import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Planetas_del_sistema_solar"
respuesta = requests.get(url)
sopa = BeautifulSoup(respuesta.text, 'html.parser')


tablas = pd.read_html(respuesta.text)


for i, tabla in enumerate(tablas):
    print(f"Tabla {i}:")
    print(tabla.head())
    print("=" * 50)


tabla_correcta = tablas[3]  


df = tabla_correcta[["Planeta enano", "Satélites naturales"]]
df.columns = ["Planeta Enano", "Satélites Naturales"]


df = df.dropna()
df = df[df["Satélites Naturales"].astype(str).str.isnumeric()]
df["Satélites Naturales"] = df["Satélites Naturales"].astype(int)
df.reset_index(drop=True, inplace=True)


print("\nResultado final:")
print(df)


df.to_csv("planetas_enanos.csv", index=False)
print("\nArchivo CSV guardado como planetas_enanos.csv")
