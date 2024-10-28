
Please go to openai.com open an account and get an apikey. you will need an pay account since the free account is only good for $5.00
you can set maxtoken=200 in the function

please set up an .env file ins your code folder to place the api key

OPEN_API_KEY= "input your api key"

create virtual enviroment file in your code folder

https://www.youtube.com/watch?v=yG9kmBQAtW4

python -m venv ai1

source ai1/Scripts/activate  ("ai1" is the name of the file you can name it to your liking) use this for git
ai1/Scripts/activate " use this for vscode"

python -m venv filename

source filename/Scripts/activate for git

filename/Scripts/activate for vscode terminal

create virtual-venv file in your vscode terminal or pycharm

for mac  https://www.youtube.com/watch?v=Kg1Yvry_Ydk

cd my-project/
virtualenv venv

source venv/bin/activate

pip install openai
pip install datetime
pip install pyttsx3  
pip install SpeechRecognition
pip install pyaudio
pip install pygame
pip install gtts 
pip install playsound
pip isntall datetime
pip install python-dotenv
pip install numpy 
pip install pyautogen # this will have all the python repo packages.

I have set up four files Assistantbot is for your personal assistant and you can add the openai function to make it access to openai or your lm studio server.
you can change the name of your assistant to your like just look for the name Ava and replace it Jarvis.


file:talkopenai.py use pyttsxc3 tts have different voice
file:talkopenai1.py have gtts tts have different voice
file:talktolm.py use gtts

other sites 

https://openai.com/ register get the API developer account.

https://lmstudio.ai/

how to insttall vscode
https://www.youtube.com/watch?v=Bn4TuMkHmB0

how to install python on window 

https://www.youtube.com/watch?v=m9I-YpOjXVQ


I want to thank my Udemy instructors, "Arbaz Khan" and "Alexander Schlee," for providing me with the ideas to communicate with OpenAI. I learned a lot from them, and you can find their courses on Udemy.

Try experimenting to incorporate different text-to-speech (TTS) into the code to obtain new voices. Have fun!

I have added a fix to change load_dotenv() before the code to load .env file with apikey.Add two links openai.com and you tube video how to set virtual enviroment file.add mac command and update vscode venv command.
UPDATE: I have add new files requirements.txt and main4.py. 
requiremnts.txt is for all require python repo needed to be install to run the code. Make sure to activate venv inside your vs code terminal and run pip install -r requirements.txt.

main4.py file is Gradio app for openai chat window html.

I have my window desktop default to dark mode if you want to add dark mode to gradio please see code below.
****
import gradio as gr

js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

with gr.Blocks(js=js_func) as demo:
    demo.launch()
    
![Chat with Openai](https://github.com/user-attachments/assets/d8078f58-fa95-4f78-919e-4c25d51c6ae9)


Updated 10-28-2024 changed openai setting upgrade to openai=1.52. in cmd or vsc terminal pip openai-upgrade. Add import from openai import OpenAI
Add code "client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))" to set def as client
Add code  "response = client.chat.completions.create" modify def chat_lmn if you had my earlier code that used openai=0.28 version
