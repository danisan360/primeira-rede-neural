import os
import glob
import random
import shutil

def criar_pastas_e_move_formato_tensorflow():
    diretorio_atual = os.path.abspath(os.getcwd())

    pasta = "/daniel_gustavo_dataset"
    pasta_treino = diretorio_atual + pasta + "/train"
    pasta_validacao = diretorio_atual + pasta + "/validation"
    pasta_teste = diretorio_atual + pasta + "/test"

    os.mkdir(diretorio_atual + pasta)
    os.mkdir(pasta_treino) 
    os.mkdir(pasta_validacao)
    os.mkdir(pasta_teste)

    nova_pasta_treinamento_daniel = pasta_treino + "/daniel"
    nova_pasta_treinamento_gustavo = pasta_treino + "/gustavo"
    nova_pasta_validacao_daniel = pasta_validacao + "/daniel"
    nova_pasta_validacao_gustavo = pasta_validacao + "/gustavo"
    nova_pasta_teste_daniel = pasta_teste + "/daniel"
    nova_pasta_teste_gustavo = pasta_teste + "/gustavo"

    os.mkdir(nova_pasta_treinamento_daniel)
    os.mkdir(nova_pasta_treinamento_gustavo)
    print("Pastas de treinamento criadas.")
    os.mkdir(nova_pasta_validacao_daniel)
    os.mkdir(nova_pasta_validacao_gustavo)
    print("Pastas de validação criadas.")
    os.mkdir(nova_pasta_teste_daniel)
    os.mkdir(nova_pasta_teste_gustavo)
    print("Pastas de teste criadas.")

    diretorio_atual = os.path.abspath(os.getcwd())

    imagens_treinamento_daniel = glob.glob(diretorio_atual + "/daniel/" +'*.png')
    imagens_treinamento_gustavo = glob.glob(diretorio_atual + "/gustavo/" +'*.png')

    validacao_porcentagem = 0.1
    teste_porcentagem = 0.2

    for imagem in imagens_treinamento_daniel:
        
        rand = random.random()
        nome_arquivo = imagem.split("/")[-1]

        if rand <= validacao_porcentagem: 
            shutil.move(imagem, nova_pasta_validacao_daniel + "/" + nome_arquivo) 
        elif rand > teste_porcentagem and rand <= validacao_porcentagem + teste_porcentagem:
            shutil.move(imagem, nova_pasta_teste_daniel + "/" + nome_arquivo)
        else:
            shutil.move(imagem, nova_pasta_treinamento_daniel + "/" + nome_arquivo) 

    for imagem in imagens_treinamento_gustavo:

        rand = random.random()
        nome_arquivo = imagem.split("/")[-1]

        if rand <= validacao_porcentagem: 
            shutil.move(imagem, nova_pasta_validacao_gustavo + "/" + nome_arquivo) 
        elif rand > validacao_porcentagem and rand <= validacao_porcentagem + teste_porcentagem:
            shutil.move(imagem, nova_pasta_teste_gustavo + "/" + nome_arquivo)
        else:
            shutil.move(imagem, nova_pasta_treinamento_gustavo + "/" + nome_arquivo) 

    print("Arquivos movidos para suas respectivas pastas.")

    os.rmdir(diretorio_atual + "/daniel")
    print("Respositório '/daniel' excluido.")
    os.rmdir(diretorio_atual + "/gustavo")
    print("Respositório '/gustavo' excluido.")

def main():
    
    criar_pastas_e_move_formato_tensorflow()

if __name__ == "__main__":
    main()