from flask import Flask, request, render_template
from llmquestionbot import path, key, llm_params, ai_messages    
from langchain_core.messages import (
        HumanMessage,
        SystemMessage,
        AIMessage,
)

key(path)
model = llm_params()
app = Flask(__name__)
messages = [
        SystemMessage(content="You're a helpful assistant"),
]

@app.route("/request")
def api_process():
    messages.append (HumanMessage(content=request.args['prompt']))
    response = model.invoke(messages)
    messages.append(response)
    return response.content
    
@app.route("/", methods=["GET", "POST"])
def need_input():
    if "prompt" in request.form:
        messages.append (HumanMessage(content=request.args['prompt']))
        response = model.invoke(messages)
        messages.append(response)
        print(response)
    return render_template('index.html',response=response.content) 




def main():
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    main()
