import os
import tensorflow as tf
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.layers import RandomFlip, RandomRotation, RandomZoom
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

def treinamento():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    diretorio = os.path.abspath(os.getcwd())

    pasta = "/daniel_gustavo_dataset"
    train_folder = diretorio + pasta + "/train"
    val_folder = diretorio + pasta + "/validation"
    test_folder = diretorio + pasta + "/test"

    print(tf.__version__)

    train_dataset = image_dataset_from_directory(train_folder, image_size=(180, 180), batch_size=16)
    validation_dataset = image_dataset_from_directory(val_folder, image_size=(180, 180), batch_size=16)
    test_dataset = image_dataset_from_directory(test_folder, image_size=(180, 180), batch_size=16)

    model = keras.Sequential(
    [
        Rescaling(scale=1.0/255),
        RandomFlip("horizontal"),
        RandomRotation(0.1),
        RandomZoom(0.2),
    ])

    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    #model.add(MaxPooling2D(pool_size=(2, 2)))
    #model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["binary_accuracy"])

    callbacks = [
    ModelCheckpoint(
        filepath="model_reg.keras",
        save_best_only=True,
        monitor="val_loss"
    )]

    history = model.fit(train_dataset, epochs=10, validation_data=validation_dataset, callbacks=callbacks)
    return history

def plotar_graficos(history):
    accuracy = history.history["accuracy"]
    val_accuracy = history.history["val_accuracy"]
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    epochs = range(1, len(accuracy) + 1)
    plt.plot(epochs, accuracy, "r", label="Treino acc")
    plt.plot(epochs, val_accuracy, "b", label="Val acc")
    plt.xlabel("Épocas")
    plt.ylabel("%s")
    plt.title("Acurácia de Treino e Validação")
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, "r", label="Treino loss")
    plt.plot(epochs, val_loss, "b", label="Val loss")
    plt.xlabel("Épocas")
    plt.ylabel("%s")
    plt.title("Loss de Treino e Validação")
    plt.legend()
    plt.show()

def mostrar_resultador():
    model = keras.models.load_model("model_reg.keras")

    test_loss, test_acc = model.evaluate(image_dataset_from_directory((os.path.abspath(os.getcwd()) + "/daniel_gustavo_dataset/test"), image_size=(180, 180), batch_size=16))
    print(f"Test accuracy: {test_acc:.3f}")

def main():
    history = treinamento()
    plotar_graficos(history)
    mostrar_resultador()

if __name__ == "__main__":
    main()