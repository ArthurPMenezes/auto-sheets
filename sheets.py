from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def read_sheet(creds, spreadsheet_id, range_name):
    """
    Lê dados de uma planilha do Google Sheets.
    :param creds: Credenciais de autenticação.
    :param spreadsheet_id: ID da planilha.
    :param range_name: Intervalo de células a ser lido (ex: "Página1!A1:C10").
    :return: Lista de valores lidos.
    """
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        return result.get('values', [])
    except HttpError as err:
        print("Erro ao ler a planilha:", err)
        return None

def write_sheet(creds, spreadsheet_id, range_name, values):
    """
    Escreve dados em uma planilha do Google Sheets.
    :param creds: Credenciais de autenticação.
    :param spreadsheet_id: ID da planilha.
    :param range_name: Intervalo de células a ser escrito (ex: "Página1!A1").
    :param values: Lista de valores a serem escritos.
    """
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body={"values": values}
        ).execute()
        print("Dados escritos com sucesso!")
    except HttpError as err:
        print("Erro ao escrever na planilha:", err)