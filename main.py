from flask import Flask, render_template, request
from models.raw.bert import process_message as bert_process_message
from models.raw.openai import process_message as chatgpt_process_message
from models.raw.spacy import process_message as spacy_process_message


app = Flask(__name__)

models = {
    "bert": bert_process_message,
    "chatgpt": chatgpt_process_message,
    "spacy": spacy_process_message,
}


@app.route('/', methods=['GET', 'POST'])
def index():
    model_output = ''
    form_model = ''
    form_message = ''

    if request.method == 'POST':
        form_model = request.form['model']
        form_message = request.form['message']
        model_process = models.get(form_model)

        if model_process is None:
            print(f'[ERROR] Wrong model name: {form_model}')

        else:
            model_output_raw = model_process(form_message)
            model_output = '\n'.join(model_output_raw)
            print(f'[SUCCESS] Model {form_model} returned {model_output_raw}')

    return render_template('index.html', model_output=model_output, form_model=form_model, form_message=form_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8123, debug=True)
