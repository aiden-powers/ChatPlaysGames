# .env layout
APP_ID = '' \
APP_SECRET = '' \
TARGET_CHANNEL = ''

# getting the app id, secret
https://dev.twitch.tv/console \
Console > Applications > {Application's Name} Manage \
Bottom of the page shows a button "New Secret", that is your APP_SECRET.
Above that by just a bit is the label "Client ID", this is your APP_ID.

# TARGET_CHANNEL
I want to get the chat of my channel for example. \
My twitch link is https://www.twitch.tv/powers_aj \
I take the last section "powers_aj", that is my TARGET_CHANNEL