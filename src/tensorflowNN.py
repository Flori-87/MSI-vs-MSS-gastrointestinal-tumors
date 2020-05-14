from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import keras
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def readPickle(path_file):
    df = pd.read_pickle(path_file)
    display(df.head())
    return df

def createX(pandas_series):
    X = np.asarray(list(pandas_series))
    print(f"The shape of X is: {X.shape}")
    return X

def createY(df, name_column):
    df[name_column] = pd.Categorical(df[name_column], categories=["MSI","MSS"], ordered = True)
    y = df[name_column].cat.codes
    print(y.value_counts())
    print(f"The shape of y is: {y.shape}")
    return y
    
def splitTrainTest(X,y, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    return X_train, X_test, y_train, y_test

def prepareDataNN(X_train, X_test, y_train, y_test, debug, num_classes, img_rows, img_cols):
    if debug == False:
        number_channels = 1
    else: 
        number_channels = 3
    # Ask keras which format to use depending on used backend and arrange data as expected
    if K.image_data_format() == 'channels_first':
        X_train = X_train.reshape(X_train.shape[0], number_channels, img_rows, img_cols)
        X_test = X_test.reshape(X_test.shape[0], number_channels, img_rows, img_cols)
        input_shape = (number_channels, img_rows, img_cols)
    else:
        X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, number_channels)
        X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, number_channels)
        input_shape = (img_rows, img_cols, number_channels)

    # Incoming data is in uint8. Cast the input data images to be floats in range [0.0-1.0]  
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    print('X_train shape:', X_train.shape)
    print(X_train.shape[0], 'train samples')
    print(X_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return X_train, X_test, y_train, y_test, input_shape

def architectureNN(input_shape, num_classes):
## This is the neural network proposed architecture
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                    activation='relu',
                    input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adadelta(),
                metrics=['accuracy'])
    return model

def fitModel(model, X_train, y_train, X_test, y_test, batch_size, epochs):
    model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(X_test, y_test))
    return model