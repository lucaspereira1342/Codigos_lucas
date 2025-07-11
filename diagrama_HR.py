import matplotlib.pyplot as plt
import pandas as pd
import mesa_web as mesa

# Dicionário com os caminhos e rótulos
modelos = {
    "1 M☉, Z=0.001": r"C:\Users\lucas\Desktop\Projects\Outros_trabalhos\1-5(0.02-0.001)\1MO-0.001\trimmed_history.data",
    "1 M☉, Z=0.02":   r"C:\Users\lucas\Desktop\Projects\Outros_trabalhos\1-5(0.02-0.001)\1MO-0.02\trimmed_history.data",
}

modelos_02 = {
    "5 M☉, Z=0.001":  r"C:\Users\lucas\Desktop\Projects\Outros_trabalhos\1-5(0.02-0.001)\5MO-0.001\trimmed_history.data",
    "5 M☉, Z=0.02":   r"C:\Users\lucas\Desktop\Projects\Outros_trabalhos\1-5(0.02-0.001)\5MO-0.02\trimmed_history.data",
}

# Cores diferentes para cada modelo
cores = ['blue', 'cyan']
cores_02 = [ 'red', 'deeppink']

plt.figure(figsize=(10, 7))

for (label, caminho), cor in zip(modelos.items(), cores):
    hist = mesa.read_history(caminho)
    df = pd.DataFrame({k: v for k, v in hist.items() if hasattr(v, '__len__')})

    # Aplica o corte apenas ao modelo "1 M☉, Z=0.001"
    if label == "1 M☉, Z=0.001":
        df = df[200:-500]  # Remove os últimos 50 pontos
    elif label == "1 M☉, Z=0.02":
        df = df[131:-900]  # Remove os últimos 50 pontos
    

    # Divide o DataFrame em duas partes
    corte = int(len(df) * 0.01)  # 99% da evolução com linha sólida, 1% com tracejada
    df_sólido = df.iloc[corte:]
    df_tracejado = df.iloc[:corte]

    # Parte sólida
    plt.plot(df_sólido['log_Teff'], df_sólido['log_L'], color=cor, linewidth=1.2, label=label)
    # Parte tracejada (sem repetir o label para não duplicar na legenda)
    plt.plot(df_tracejado['log_Teff'], df_tracejado['log_L'], color=cor, linewidth=1.2, linestyle='--')

    # === Marcas no gráfico ===
    if label == "1 M☉, Z=0.001":
        i_psp = 10
        teff_psp = df.iloc[i_psp]['log_Teff']
        lum_psp = df.iloc[i_psp]['log_L']
        plt.text(teff_psp + 0.02, lum_psp, "Pré-SP", fontsize=11, color='k')
    elif label == "1 M☉, Z=0.02":
        i_psp = 60
        teff_psp = df.iloc[i_psp]['log_Teff']
        lum_psp = df.iloc[i_psp]['log_L']
        plt.text(teff_psp + 0.02, lum_psp, "Pré-SP", fontsize=11, color='k')

    if label == "1 M☉, Z=0.001":
        i_sp = 100
        teff_sp = df.iloc[i_sp]['log_Teff']
        lum_sp = df.iloc[i_sp]['log_L']
        plt.text(teff_sp + 0.02, lum_sp, "SP", fontsize=11, color='k')
    elif label == "1 M☉, Z=0.02":
        i_sp = 131
        teff_sp = df.iloc[i_sp]['log_Teff']
        lum_sp = df.iloc[i_sp]['log_L']
        plt.text(teff_sp + 0.02, lum_sp, "SP", fontsize=11, color='k')
    
    if label == "1 M☉, Z=0.001":
        i_rgb = int(len(df) * 0.05)
        teff_rgb = df.iloc[i_rgb]['log_Teff']
        lum_rgb = df.iloc[i_rgb]['log_L']
        plt.text(teff_rgb + 0.02, lum_rgb, "RGB", fontsize=11, color='k')
    elif label == "1 M☉, Z=0.02":
        i_rgb = int(len(df) * 0.06)
        teff_rgb = df.iloc[i_rgb]['log_Teff']
        lum_rgb = df.iloc[i_rgb]['log_L']
        plt.text(teff_rgb + 0.02, lum_rgb, "RGB", fontsize=11, color='k')

    if label == "1 M☉, Z=0.001":
        i_agb = -1000
        teff_agb = df.iloc[i_agb]['log_Teff']
        lum_agb = df.iloc[i_agb]['log_L']
        plt.text(teff_agb + 0.02, lum_agb, "AGB", fontsize=11, color='k')
    elif label == "1 M☉, Z=0.02":
        i_agb = -1000
        teff_agb = df.iloc[i_agb]['log_Teff']
        lum_agb = df.iloc[i_agb]['log_L']
        plt.text(teff_agb + 0.02, lum_agb, "AGB", fontsize=11, color='k')

    

for (label, caminho), cor in zip(modelos_02.items(), cores_02):
    hist = mesa.read_history(caminho)
    df = pd.DataFrame({k: v for k, v in hist.items() if hasattr(v, '__len__')})

    # Aplica o corte apenas ao modelo "1 M☉, Z=0.001"
    if label == "5 M☉, Z=0.001":
        df = df[221:-9000]  # Remove os últimos 50 pontos
    elif label == "5 M☉, Z=0.02":
        df = df[180:-7000]  # Remove os últimos 50 pontos

    # Divide o DataFrame em duas partes
    corte = int(len(df) * 0.03)  # 99% da evolução com linha sólida, 1% com tracejada
    df_sólido = df.iloc[corte:]
    df_tracejado = df.iloc[:corte]

    # Parte sólida
    plt.plot(df_sólido['log_Teff'], df_sólido['log_L'], color=cor, linewidth=1.2, label=label)
    # Parte tracejada (sem repetir o label para não duplicar na legenda)
    plt.plot(df_tracejado['log_Teff'], df_tracejado['log_L'], color=cor, linewidth=1.2, linestyle='--')

    if label == "5 M☉, Z=0.001":
        i_psp = 15
        teff_psp = df.iloc[i_psp]['log_Teff']
        lum_psp = df.iloc[i_psp]['log_L']
        plt.text(teff_psp + 0.02, lum_psp, "Pré-SP", fontsize=11, color='k')
    elif label == "5 M☉, Z=0.02":
        i_psp = 50
        teff_psp = df.iloc[i_psp]['log_Teff']
        lum_psp = df.iloc[i_psp]['log_L']
        plt.text(teff_psp + 0.02, lum_psp, "Pré-SP", fontsize=11, color='k')

    if label == "5 M☉, Z=0.001":
        i_sp = 200
        teff_sp = df.iloc[i_sp]['log_Teff']
        lum_sp = df.iloc[i_sp]['log_L']
        plt.text(teff_sp + 0.02, lum_sp, "RGB", fontsize=11, color='k')
    elif label == "5 M☉, Z=0.02":
        i_sp = 215
        teff_sp = df.iloc[i_sp]['log_Teff']
        lum_sp = df.iloc[i_sp]['log_L']
        plt.text(teff_sp + 0.02, lum_sp, "RGB", fontsize=11, color='k')
    
    if label == "5 M☉, Z=0.001":
        i_rgb = int(len(df) * 0.05)
        teff_rgb = df.iloc[i_rgb]['log_Teff']
        lum_rgb = df.iloc[i_rgb]['log_L']
        plt.text(teff_rgb + 0.02, lum_rgb, "SP", fontsize=11, color='k')
    elif label == "5 M☉, Z=0.02":
        i_rgb = int(len(df) * 0.06)
        teff_rgb = df.iloc[i_rgb]['log_Teff']
        lum_rgb = df.iloc[i_rgb]['log_L']
        plt.text(teff_rgb + 0.02, lum_rgb, "SP", fontsize=11, color='k')
    
    if label == "5 M☉, Z=0.001":
        i_agb = 530
        teff_agb = df.iloc[i_agb]['log_Teff']
        lum_agb = df.iloc[i_agb]['log_L']
        plt.text(teff_agb + 0.02, lum_agb, "AGB", fontsize=11, color='k')
    elif label == "5 M☉, Z=0.02":
        i_agb = 570
        teff_agb = df.iloc[i_agb]['log_Teff']
        lum_agb = df.iloc[i_agb]['log_L']
        plt.text(teff_agb + 0.02, lum_agb, "AGB", fontsize=11, color='k')




# Inverte o eixo x
plt.gca().invert_xaxis()

# Labels e estilo
plt.xlabel(r'$\log\,T_{\mathrm{eff}}$ [K]')
plt.ylabel(r'$\log\,L/L_\odot$')
plt.title("Diagramas HR comparativos (MESA-Web)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
