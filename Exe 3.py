#3.Crie uma lista com os 20 primeiros colocados
j =[]
vetor_time = ['Palmeiras','Santos','Atletico-MG','Botafogo',
              'Flamengo','Bahia','Internacional','São Paulo',
              'Goias','Corinthians','Athelico-PR','Ceara',
              'Gremio', 'Cruzeiro','Fluminense','Chapecoense',
               'Fortaleza','Vasco','CSA','Avai']
#a. 5 Primeiros Colocados
print("Os cinco primeiros colocados são:", vetor_time[0:5],"\n")

#b. Zona de Rebeixamento
print("Os Times na Zona de Rebaixamento são:", vetor_time[16:20],"\n")

#c. mostre a posição em que se encontra a chapecoense
print("A Posição da Chape eh:", vetor_time.index('Chapecoense'),"\n")
#d. Exiba a lista dos times em ordem alfabética
vetor_time.sort()
print(vetor_time)