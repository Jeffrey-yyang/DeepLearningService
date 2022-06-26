from flask import Flask, request
from models import ModelLoad

app = Flask(__name__)
dl_models = ModelLoad()


@app.route("/summarizer")
def extract_summary():
    content = request.args.get("content", "")
    max_length = request.args.get("maxlength", 300)
    min_length = request.args.get("minlength", 50)
    result = dl_models.summarizer(content, max_length=int(max_length), min_length=int(min_length), do_sample=False)
    if result:
        summary = result[0].get("summary_text")
    else:
        summary = ""
    return summary


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(debug=True)
