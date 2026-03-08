from flask import Flask, render_template, request
from transformers import pipeline


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['input_text']
        classifier = pipeline('sentiment-analysis')
        result = classifier(text)
        return render_template('analyze.html', result=result, text=text)

    return render_template('analyze.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        text = request.form['input_text']
        generator = pipeline('text-generation')
        result = generator(text, num_return_sequences=1, max_new_tokens=500)
        return render_template('generate.html', result=result, text=text)

    return render_template('generate.html')



if __name__ == '__main__':
    app.run(debug=True)