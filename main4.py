from dotenv import load_dotenv
import os
import gradio as gr
import openai

load_dotenv()


openai.api_key = os.getenv("OPEN_API_KEY")
MODEL= "gpt-4o-mini"


def generate_output(prompt, history):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    assistant_response = response.choices[0].message.content
    return [("assistant", assistant_response)],history



prompt = "Enter a message to chat with the AI"



def chat_lm(input, history):
    history = history or []
    if input.strip() != "":
        combined_input = ' '.join(history + [input])
        output_text = generate_output(input, history)
        history.append(input)
        output = [("user", input)] + output_text
    else:
        output = []
    return history, [output]



block = gr.Blocks()
with block:
    gr.Markdown("""<h1><center>Chat with OpenAI</center></h1>""")
    chatbot = gr.Chatbot(height=550)
    message = gr.Textbox(placeholder=prompt,type="text",label="Message",)
    submit = gr.Button("SEND")
    state = gr.State()
    submit.click(generate_output,inputs=[message,state],outputs=[chatbot,state])




block.launch(debug=True)
