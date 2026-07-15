from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RAG Based AI Teaching Assistant"

if __name__ == "__main__":
    app.run(debug=True)
