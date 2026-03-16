# FarmTech Solutions - Estatísticas Básicas

# === CAFÉ ===
acafe <- c(10000, 80421, 38402)       # áreas de plantio (m²)
cinsumo <- c(90, 80, 281)             # insumos utilizados (L)
minsumocafe <- mean(cinsumo)          # média de insumos do café
dpcafe <- sd(acafe)                   # desvio padrão da área do café

print(paste("Média de insumos de café necessária:", round(minsumocafe, 2)))
print(paste("Desvio padrão da área da lavoura de café:", round(dpcafe, 2)))

# === SOJA ===
sinsumo <- c(90, 281, 289)            # insumos utilizados (L)
minsumosoja <- mean(sinsumo)          # média de insumos da soja

print(paste("Média de insumos de soja necessária:", round(minsumosoja, 2)))

