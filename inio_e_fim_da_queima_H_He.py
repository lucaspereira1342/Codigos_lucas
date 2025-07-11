arquivo = r"C:\Users\lucas\Desktop\Projects\Outros_trabalhos\1-5(0.02-0.001)\5MO-0.001\trimmed_history.data"  # Altere se necessário

# Função para ler o arquivo ignorando os comentários e cabeçalhos
def ler_history(path):
    with open(path, 'r') as f:
        linhas = f.readlines()

    for i, linha in enumerate(linhas):
        if "model_number" in linha:
            header_index = i
            break

    colunas = linhas[header_index].strip().split()
    df = pd.read_csv(path, delim_whitespace=True, comment="#",
                     skiprows=header_index + 1, names=colunas)
    return df

# Lê os dados
df = ler_history(arquivo)

# Inicializa os eventos como None
eventos = {
    "inicio_queima_H": None,
    "fim_queima_H": None,
    "inicio_queima_He": None,
    "fim_queima_He": None,
}

# Loop pelos modelos
for i in range(len(df)):
    h = df.loc[i, "center_h1"]
    he = df.loc[i, "center_he4"]
    model = df.loc[i, "model_number"]
    idade = df.loc[i, "star_age"]

    if eventos["inicio_queima_H"] is None and h < 0.7:
        eventos["inicio_queima_H"] = (model, idade, h)

    if eventos["fim_queima_H"] is None and h < 1e-6:
        eventos["fim_queima_H"] = (model, idade, h)

    if eventos["fim_queima_H"] and eventos["inicio_queima_He"] is None and he < 0.95:
        eventos["inicio_queima_He"] = (model, idade, he)

    if eventos["inicio_queima_He"] and eventos["fim_queima_He"] is None and he < 1e-6:
        eventos["fim_queima_He"] = (model, idade, he)

# Exibe os resultados
for evento, info in eventos.items():
    if info:
        model, idade, valor = info
        print(f"{evento.replace('_', ' ').capitalize()}: modelo {model}, idade {idade:.2e} anos, valor = {valor:.2e}")
    else:
        print(f"{evento.replace('_', ' ').capitalize()}: não detectado.")
