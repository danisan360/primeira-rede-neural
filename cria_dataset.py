import os
import glob
import cv2
import numpy as np

def cria_pastas(pastas):
    for pasta in pastas:
        try:
            os.mkdir(pasta)
            print("Diretório ", pasta," foi criado.")
        except OSError:
            print("Diretório ", pasta," já existe.")


def cria_imagens(pasta ,contador_de_imagens):
    diretorio_atual = os.path.abspath(os.getcwd())

    arquivos = []
    for arquivo in glob.glob(diretorio_atual + "/videos/" + pasta + "/*.mp4"):
        arquivos.append(arquivo)

    print(arquivos)

    for arquivo in arquivos:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        video = cv2.VideoCapture(arquivo)
        if (video.isOpened()== False): 
            print("Erro carregando o video.")
        else:
            print("Video carregado com sucesso!")
            print("Analisando o vídeo: ", arquivo)

        while(1):
            sucesso, frame = video.read()

            if (sucesso == False):
                video.release()
                break

            faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.3, 5)

            if (np.any(faces) == False):
                continue

            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]

            larg, alt, _ = face.shape  # Adicionado um filtro de tamanho da face, pois faces muito pequenas normalmente eram erros e gerava muito ruído.
            if(larg * alt <= 20 * 20):
                continue
            
            face = cv2.resize(face, (255, 255))
            cv2.imwrite(pasta + "/" + str(contador_de_imagens)+".png", face)
            print("Criada a imagem: ", str(contador_de_imagens), ".png")
            contador_de_imagens += 1
        
        video.release()
    
    return (contador_de_imagens + 1)


def main():
    pastas = ["daniel", "gustavo"]
    cria_pastas(pastas)

    contador_de_imagens = 0
    for pasta in pastas:
        contador_de_imagens = cria_imagens(pasta, contador_de_imagens)

    

if __name__ == "__main__":
    main()