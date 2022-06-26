from transformers import pipeline


class ModelLoad(object):
    def __init__(self):
        self.summarizer = self.load_summarization_model()

    def load_summarization_model(self):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        return summarizer

    def load_densenet_model(self):
        pass
