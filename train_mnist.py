import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models, losses, Model
import gc 

def train_NN(optimizer_method, lr, epochs, batch_size):
    (x_train, y_train), (x_test, y_test)=tf.keras.datasets.mnist.load_data()
    x_train = tf.pad(x_train, [[0, 0], [2,2], [2,2]])/255
    x_test = tf.pad(x_test, [[0, 0], [2,2], [2,2]])/255
    x_train = tf.expand_dims(x_train, axis=3, name=None)
    x_test = tf.expand_dims(x_test, axis=3, name=None)
    x_train = tf.repeat(x_train, 3, axis=3)
    x_test = tf.repeat(x_test, 3, axis=3)
    
    x_train = x_train[:-2000,:,:]
    y_train = y_train[:-2000]

    x_train=x_train[:25000]
    y_train=y_train[:25000]

    x_test=x_test[:6000]
    y_test=y_test[:6000]

    model = models.Sequential()
    model.add(layers.experimental.preprocessing.Resizing(224, 224, interpolation="bilinear", input_shape=x_train.shape[1:]))
    model.add(layers.Conv2D(64, 3, strides=2, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D(2, strides=2))
    model.add(layers.Conv2D(128, 3, strides=2, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D(2, strides=2))
    model.add(layers.Flatten())
    model.add(layers.Dense(2048, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(10, activation='softmax'))
   

    if optimizer_method=="Adam":
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr)
    elif optimizer_method=="SGD":
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr)
    else:
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001)

    model.compile(optimizer=optimizer, loss=losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    
    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

    score = history.history['val_accuracy'][-1]
    
    del x_train, y_train, x_test, y_test
    gc.collect()
    
    tf.keras.backend.clear_session()
 
    return score