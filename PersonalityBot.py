import random

responses = {
    "AoA": [
        "WalaikumAsSalam. Kesy hain ap?",
        "Walaikum. Hukum kren"
    ],
    "Ma theek hn ap sunaen": [
        "Duaen hn ap ki",
        "Alhumdulillah"
    ],
    "Ap ka naam kia ha?": [
        "Allah Deta",
        "Naa cheez ko Allah Deta kehty hn",
    ]
}


def respond(message):
    if message in responses:
        return random.choice(responses[message])


if __name__ == "__main__":
    print("Muqaalma shuru kren..")
    message = input()
    while message != "AllahHafiz":
        print(respond(message))
        message = input()
