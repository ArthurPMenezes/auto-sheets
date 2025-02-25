from auth import authenticate
from sheets import read_sheet, write_sheet

def main():
    # Autentica no Google Sheets
    creds = authenticate()

    # ID da planilha (substitua pelo ID da sua planilha)
    spreadsheet_id = "1C5U6MY0mLiGUDvdYUeSEycvH5S-Yl5P6lDhQBGX5LaI"

    # Ler dados da planilha
    print("Lendo dados da planilha...")
    data = read_sheet(creds, spreadsheet_id, "Página1!A1:C10")
    print("Dados lidos:", data)

    # Escrever dados na planilha
    print("Escrevendo dados na planilha...")
    novos_dados = [
        ["Dezembro", "R$ 50.000,00"],
        ["Janeiro/22", "R$30.000,00"],
        ["Fevereiro/22", "R$127.552,00"],
    ]
    write_sheet(creds, spreadsheet_id, "Página1!A13", novos_dados)

if __name__ == "__main__":
    main()