from app import create_app

app = create_app()
if __name__ == '__main__':
    print("6000")
    app.run(host="0.0.0.0", port=6000)
