import pandas as pd

df_costos = pd.read_csv('./data/dfsample/costos.csv', dtype={'ID':str})
 # Are you using your dataframe with Choropleth maps?
 # If your polygon gejson use code with leading zeros, define zfill with the number of zeros required.
 #df_costos['ID'] = df_costos['ID'].str.zfill(2)

df_opsales = pd.read_csv('./data/dfsample/opsales.csv')

df_markers = pd.read_csv('./data/dfsample/markers.csv')

# dataset de prueba para el mapa
datatest ={'DEPARTAMENTO': ['SANTANDER', 'ANTIOQUIA', 'CUNDINAMARCA', 'BOYACA'], 
       'COUNT':[99, 900, 9000,900000], 
       'COD_DPTO':['68', '05', '25','15']} 
 # Are you using your dataframe with Choropleth maps?
 # If your polygon gejson use code with leading zeros, define zfill with the number of zeros required.
 #df_costos['ID'] = df_costos['ID'].str.zfill(2)
  
df_maptest = pd.DataFrame.from_dict(datatest)  
