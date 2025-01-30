from flask import Flask, request, render_template
from llmquestionbot import path, key, llm_params, ai_messages    

key(path)
model = llm_params()
app = Flask(__name__)


@app.route("/request")
def api_process():
    response = ai_messages(model, request.args['prompt'])
    return response
    

@app.route("/")
def hello_world():
    return render_template('index.html')
    

def main():
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    main()
