# Se importan los archivos necesarios
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Se leen los archivos parquet desde los vínculos
transacciones_df = pd.read_parquet('https://datamxdevsa.blob.core.windows.net/crskmex000/DSTest/0saldos.parquet')
saldos_df = pd.read_parquet('https://datamxdevsa.blob.core.windows.net/crskmex000/DSTest/0transferencias.parquet')
clientes_df = pd.read_parquet('https://datamxdevsa.blob.core.windows.net/crskmex000/DSTest/0clientes.parquet')

# Se unen las tablas en un solo DataFrame
merged_df = pd.merge(transacciones_df, saldos_df, on=['Contrato'])   #, 'CLIENTE', 'PRODUCTO'])
merged_df = pd.merge(merged_df, clientes_df, on='NroDocum')
