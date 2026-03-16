library(httr)
library(jsonlite)

url <- "https://api.open-meteo.com/v1/forecast?latitude=-23.52&longitude=-46.18&current_weather=true"
resposta <- GET(url)

conteudo <- content(resposta, as = "text")
dados <- fromJSON(conteudo)

clima <- dados$current_weather

print(paste("Temperatura atual: ", round(clima$temperature , 2)))
print(paste("Velocidade do vento: ", round(clima$windspeed, 2)))
print("Se estiver de dia a resposta será 1, se estiver de noite a resposta será 0: ")
print(paste(clima$is_day))

