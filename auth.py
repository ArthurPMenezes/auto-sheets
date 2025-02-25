from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path

# Escopos necessários para acessar o Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def authenticate():
    """
    Autentica no Google Sheets e retorna as credenciais.
    Se o token.json existir, usa ele. Caso contrário, inicia o fluxo de autenticação.
    """
    creds = None
    # Verifica se o token.json já existe
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # Se não houver credenciais válidas, inicia o fluxo de autenticação
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Atualiza o token se expirado
        else:
            # Inicia o fluxo de autenticação
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para uso futuro
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds