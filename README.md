# Sentiment-Analysis-Web-App
A Flask-based application that allows users to perform sentiment analysis on text input through a web interface. The app takes user input from an HTML page, processes it using a sentiment analysis model, and returns the sentiment label along with its confidence score.

The HTML file (index.html) for the frontend of the app is stored in the **'templates'** folder, the JavaScript file (script.js), and the CSS file (style.css) is stored in the **'static'** folder.


# Features
- Web Interface: User-friendly HTML interface for inputting text.
- Real-Time Sentiment Analysis: Analyze text sentiment in real-time using a pre-trained sentiment analysis model.
- Flask-based Deployment: The app runs on a Flask server and is accessible via 'localhost:5000'

# Requirements

I created a virtual environment using Anaconda and installed all required libraries in the environment

python version : 3.12.4

conda version : 24.7.1

Check out the 'REQUIREMENTS.TXT' file for more info on the required libraries and python packages

# Code Explanation

The server.py file imports the 'sentiment_analyzer' function from the *sentiment_analysis.py* file in the folder 'SentimentAnalysis'.

- `app = Flask("Sentiment Analysis")` : Initializes the Flask application with the name "Sentiment Analysis".

- `@app.route("/sentimentAnalyzer")` :This route handles the sentiment analysis and is the API endpoint. It retrieves the text input from the request, passes it to the sentiment_analyzer function, and returns the analysis result.

- `@app.route("/")` : This route renders the main application page (index.html).

- `__name__ == "__main__"` : This allows the Flask app to only run when this python script is run directly, not when it is imported into another module

- `app.run(host="0.0.0.0", port=5000)` : Starts the Flask server, making the app accessible via localhost:5000.

- `sentiment_analyzer(text_to_analyze)` : This function analyzes the provided text and return a dictionary with the sentiment label and confidence score. The Flask app uses this function to process text input from the user.

# Final Result
Web App Interface:

![image](https://github.com/user-attachments/assets/b6f64b08-ccce-4e49-aa6c-e95788a4d868)

Sentiment Analysis result:

![image](https://github.com/user-attachments/assets/79d44f02-f20b-4245-aa1c-56a2115bacb3)


