
"""
Módulo de Conexão com Google Drive (Infraestrutura).
Define a "Zona de Sinergia" (Pasta Isolada) como base operacional do Agente.
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json

# CONFIGURAÇÃO DA BASE OPERACIONAL
# Esta pasta é o "Universo Observável" do Agente no Google Drive.
PASTA_ID = "1ntgLeGPzSirl6Kl4V1UnnnyvPA8ZC2un" 

# Configurações de Autenticação
SCOPES = ['https://www.googleapis.com/auth/drive']
KEY_FILE = 'credentials.json' # Deve estar na raiz do projeto

class DriveConnector:
    def __init__(self):
        self.service = self._connect()
        self.base_folder_id = PASTA_ID

    def _connect(self):
        """Estabelece conexão segura com a Service Account."""
        if not os.path.exists(KEY_FILE):
            print(f"[DRIVE] ERRO CRÍTICO: Chave '{KEY_FILE}' não encontrada.")
            print("[DRIVE] Por favor, coloque o arquivo JSON baixado do Google Cloud na raiz do projeto.")
            return None

        try:
            creds = service_account.Credentials.from_service_account_file(
                KEY_FILE, scopes=SCOPES)
            service = build('drive', 'v3', credentials=creds)
            print("[DRIVE] Conexão estabelecida com sucesso (Identidade Robô).")
            return service
        except Exception as e:
            print(f"[DRIVE] Falha na conexão: {e}")
            return None

    def list_files(self):
        """Lista arquivos APENAS dentro da Base Operacional (Zona de Sinergia)."""
        if not self.service: return []

        try:
            # Query filtra por 'parents' igual ao ID da pasta segura
            results = self.service.files().list(
                q=f"'{self.base_folder_id}' in parents and trashed=false",
                pageSize=20, 
                fields="nextPageToken, files(id, name, mimeType)"
            ).execute()
            
            items = results.get('files', [])
            if not items:
                print('[DRIVE] A Zona de Sinergia está vazia.')
            else:
                print(f'[DRIVE] Arquivos encontrados na Base Operacional ({len(items)}):')
                for item in items:
                    print(f" -> {item['name']} ({item['mimeType']})")
            return items
        except Exception as e:
            print(f"[DRIVE] Erro ao listar arquivos: {e}")
            return []

    def upload_file(self, local_path, remote_name=None):
        """Faz upload de um arquivo local para a Base Operacional."""
        if not self.service: return None
        
        from googleapiclient.http import MediaFileUpload
        
        if not remote_name:
            remote_name = os.path.basename(local_path)

        file_metadata = {
            'name': remote_name,
            'parents': [self.base_folder_id] # Força o upload PARA DENTRO da pasta segura
        }
        
        media = MediaFileUpload(local_path, resumable=True)
        
        try:
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print(f"[DRIVE] Upload concluído: {remote_name} (ID: {file.get('id')})")
            return file.get('id')
        except Exception as e:
            print(f"[DRIVE] Erro no upload: {e}")
            return None

# Teste de Conexão (Executado se rodar direto)
if __name__ == "__main__":
    connector = DriveConnector()
    if connector.service:
        print(f"--- Explorando Base Operacional: {PASTA_ID} ---")
        connector.list_files()
