from datetime import date, datetime
import pyttsx3
import speech_recognition


my_name = "William Lam Nguyen"
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
# default voice is male voice.
# below code will change voices to female voice
# but female voice is too fast and the voice is not clearly
# voices = robot_mouth.getProperty('voices')
# robot_mouth.setProperty('voice', voices[1].id)

def printRobot(msg):
    print("Robot: " + msg)

def printYou(msg):
    print("You: " + msg)

# --------
# LISTEN
# --------
def listen():
    with speech_recognition.Microphone() as mic:
        listening = "May i help you?"
        say(listening)
        audio = robot_ear.listen(mic)

    printRobot("...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "You said nothing"

    printYou(you)
    return you

# --------
# UNDERSTAND
# --------
def understand(you):
    if you == "":
        robot_brain = "I can't hear you, please try again"
    elif "who am" in you:
        robot_brain = "I sure that you are " + my_name
    elif "hello" in you:
        robot_brain = "Hello " + my_name
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "wife" in you:
        robot_brain = "Any beautiful girls, but not Tram Phan"
    elif "bye" in you:
        robot_brain = "Bye " + my_name
        say(robot_brain)
        return False
    else:
        robot_brain = "I can't hear you, please try again"

    return robot_brain

# --------
# SAY
# --------
def say(robot_brain):
    printRobot(robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    robot_mouth.stop()

# --------
# main
# --------
say("My name is Lucy")

while True:
    you = listen()
    robot_brain = understand(you)

    if robot_brain == False:
        break

    say(robot_brain)