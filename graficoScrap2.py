import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv('Cordoba_Eventos.csv', sep=',')
df_fecha = df['Fecha'].iloc[19:45]
df_eventos = df['Evento'].iloc[19:45]

#Creamos una lista con los eventos
eventos = df_eventos
y_pos = np.arange(len(eventos))

#Fechas de los Eventos
fechas_eventos = df_fecha

plt.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'font.size': 8,
        'mathtext.fontset': 'stix',
    }
)


#Creamos la grafica 
plt.barh(y_pos, fechas_eventos,color = 'purple' ,alpha=0.8)

#etiqueta y
plt.yticks(y_pos, eventos)

#etiqueta x
plt.xlabel('Fechas')


#Titulo
plt.title('Eventos en Cordoba')
plt.savefig('./base_datos/grafico_scrap2.png', bbox_inches='tight',dpi=600)
plt.show()