from models.utils import *


def SDFCN(input_size=(imageSize,imageSize,Channels)):
    inputs = Input(input_size)
    conv1_1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1_2 = Conv2D(64, 3, activation='relu', padding='same')(conv1_1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1_2)

    sc2 = shortcutblock(128,1)(pool1)
    pool2 = MaxPooling2D(pool_size=(2, 2))(sc2)

    sc3 = shortcutblock(256,2)(pool2)
    pool3 = MaxPooling2D(pool_size=(2, 2))(sc3)

    sc4 = shortcutblock(512,3)(pool3)
    sc4 = shortcutblock(512,4)(sc4)

    conv5_1 = Conv2DTranspose(256, 3, strides=2, padding='same')(Concatenate()([sc4, pool3]))
    conv5_2 = shortcutblock(256,5)(conv5_1)

    conv6_1 = Conv2DTranspose(128, 3, strides=2, padding='same')(Concatenate()([conv5_2, pool2]))
    conv6_2 = shortcutblock(128,6)(conv6_1)

    conv7_1 = Conv2DTranspose(64, 3, strides=2, padding='same')(Concatenate()([conv6_2, pool1]))
    conv7_2 = Conv2D(64, 3, activation='relu', padding='same')(conv7_1)
    conv7_3 = Conv2D(64, 3, activation='relu', padding='same')(conv7_2)

    # softmax
    conv8 = Conv2D(Classes, 1, activation='softmax')(conv7_3)

    model = Model(inputs, conv8)

    return model