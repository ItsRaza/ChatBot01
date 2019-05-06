import time


def respond(message):
    time.sleep(0.5)
    return "Message recieved '{}'".format(message)


def send_message(message):
    print("USER: {}".format(message))
    print("BOT:", respond(message))


if __name__ == "__main__":
    print("Send message to echoBot..")
    message = input()
    send_message(message)
