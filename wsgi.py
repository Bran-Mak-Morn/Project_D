from app import create_app # import aplikační továrny

app = create_app() # vytvoření objektu pomocí funkce pro vytvoření aplikační továrny

if __name__ == "__main__":
    app.run(host='0.0.0.0')