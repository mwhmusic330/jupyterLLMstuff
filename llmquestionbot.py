from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
import getpass, os
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

path="/home/michael/hugginfacestuff/token2"

def key(path):
    with open(path, 'r') as f: 
        apikey = f.read().strip()
    if not apikey:
        with open(path, 'w') as f:
            apikey = getpass.getpass(
                "Enter your Hugging Face API key: "
            )
            f.write(apikey)
           
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = apikey




def llm_params():
    llm = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        max_new_tokens=10000,
        do_sample=False,
        repetition_penalty=1.03,
    )

    chat_model = ChatHuggingFace(llm=llm)
    
    return chat_model

def ai_messages(chat_model, prompt):
    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content=prompt),
    ]

    ai_msg = chat_model.invoke(messages)

    return ai_msg.content



def main():
    keyfunc = key(path)
    model = llm_params()
    messageparams = ai_messages(model)

if __name__ == '__main__':
    main()
