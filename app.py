from flask import Flask, request
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/summarizer")
def extract_summary():
    content = request.args.get("content", "")
    max_length = request.args.get("maxlength", 300)
    min_length = request.args.get("minlength", 50)
    result = summarizer(content, max_length=int(max_length), min_length=int(min_length), do_sample=False)
    if result:
        summary = result[0].get("summary_text")
    else:
        summary = ""
    return summary


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(host='0.0.0.0', debug=True)
