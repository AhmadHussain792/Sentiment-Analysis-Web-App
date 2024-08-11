from transformers import pipeline

model = pipeline("sentiment-analysis")

def sentiment_analyzer(text_to_analyze):
    if text_to_analyze == "":
        output = "Invalid entry! try again"
    else:
        output = model(text_to_analyze)[0]

    return output
