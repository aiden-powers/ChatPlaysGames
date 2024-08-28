![image](https://github.com/user-attachments/assets/f5f3595d-8163-44d6-96f4-451a081f5e8e)

# Code
before you start main.py, make sure you have a .env file.

### .env layout
APP_ID = '' \
APP_SECRET = '' \
TARGET_CHANNEL = ''

### getting the app id, secret
https://dev.twitch.tv/console \
Console > Applications > {Application's Name} Manage \
Bottom of the page shows a button "New Secret", that is your APP_SECRET.
Above that by just a bit is the label "Client ID", this is your APP_ID.

### TARGET_CHANNEL
I want to get the chat of my channel for example. \
My twitch link is https://www.twitch.tv/powers_aj \
I take the last section "powers_aj", that is my TARGET_CHANNEL

# How To Start
Start peggle and make sure the window is open before running main.py \
Closing peggle before closing main.py will make main freak out.

### What about the other files?
The other files act as classes and functions. Main.py is the only way to start the chat code.
