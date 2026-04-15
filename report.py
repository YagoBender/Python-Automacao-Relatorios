def generate_report(data):
    with open("relatorio.txt", "w") as f:
        for item in data:
            f.write(f"{item}\n")
