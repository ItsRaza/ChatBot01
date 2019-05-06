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
        "A girl has no name"
    ],
    "Ziada shaloo paloo hony ka zrort nai ha": "he he. mazak tha.."
}

wrongQueries = [
    "Arey kehna kia chaty hoe?..",
    "I beg your pardon",
    "Ap pagal ho kia?"
]


def respond(message):
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(wrongQueries)


if __name__ == "__main__":
    print("Muqaalma shuru kren..")
    message = input("USER:")
    while message != "AllahHafiz":
        print("BOT:", respond(message))
        message = input()
