from api_client import get_data
from database import save_data, fetch_data
from report import generate_report

def main():
    data = get_data()
    save_data(data)
    result = fetch_data()
    generate_report(result)
    print("Processo finalizado! Relatório gerado.")

if __name__ == "__main__":
    main()
