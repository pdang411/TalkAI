
Please get openai.com open an account and get an apikey. you will need an pay account since the free account is only good for $5.00
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

for mac 

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

https://openai.com/

https://lmstudio.ai/

I want to thank my Udemy instructors, "Arbaz Khan" and "Alexander Schlee," for providing me with the ideas to communicate with OpenAI. I learned a lot from them, and you can find their courses on Udemy.

Try experimenting to incorporate different text-to-speech (TTS) into the code to obtain new voices. Have fun!

I have added a fix to change load_dotenv() before the code to load .env file with apikey.Add two links openai.com and you tube video how to set virtual enviroment file.add mac command and update vscode venv command.
