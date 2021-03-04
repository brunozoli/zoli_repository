# -*- coding: utf-8 -*-

##1. Todas as importações
from selenium import webdriver
from time import sleep

##2. Todos os parâmetros
URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'

##3. Execução de código

if __name__ == '__main__':
    #Criar uma instância do google chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) ##tempo dado para abrir a pagina, para evitar 
    
    #Acessar URL do linkedin
    driver.get(URL_LINKEDIN_DS)
    
    #Pegar lista de resultados de vagas de ciencia de dados
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricao = []
    
    
    #Iniciar um while loop em cima de todos os resultados
    while True:
        #For loop para coletar as descrições de dados
        for r in resultados[len(lista_descricao):]:
            r.click() #Clicar na descricao
            sleep(2) #Esperar por 2 segundos, evita erro
            try:
                #Pegar elemento com  a descrição
                descricao = driver.find_element_by_class_name('description')
                #Anexar o testo na lista
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
            
        resultados = driver.find_elements_by_class_name('result-card')
        
        #Criterio de saida do while
        if len(lista_descricao) == len(resultados):
            break
 
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt','w',encoding="utf-8") as f:
        f.write(descricao_salvar)
        
    driver.quit()
