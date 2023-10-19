import openai
import gradio as gr

#coloque sau chave no local de minha_chave_api
openai.api_key = 'Minha_chave_api'

def openai_chat(prompt):
    completions = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 2000,
        n = 1,
        temperature = 0.8,
    )
    message = completions.choices[0].text
    
    return message.strip()


def chatbot(input, history=[]):
    output = openai_chat(input)
    history.append((input, output))
    return history, history


gr.Interface(fn = chatbot,
             inputs = ["text", "state"],
             outputs = ["chatbot", "state"]).launch(debug=True)