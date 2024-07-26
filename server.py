"""
server.py - A Flask web application for emotion detection.

This module sets up a Flask web server that renders an index page and provides an endpoint
for analyzing the emotions in a given text using the `emotion_detection` function from
the `EmotionDetection` package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the index page.
    
    This function renders the 'index.html' template when the root URL is accessed.
    
    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():

    """
    Analyze the emotion of the given text.
    
    This function retrieves the text to be analyzed from the request's query parameters,
    uses the emotion_detection function to analyze the text, and returns a formatted
    string with the results. If the dominant emotion is None, it returns an error message.
    
    Returns:
        str: A formatted string with the analysis results or an error message.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please, try it again"

    formatted_output = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']},"
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    # Run the Flask application on the local development server
    app.run(host="0.0.0.0", port=5000)
