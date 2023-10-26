from flask_app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
