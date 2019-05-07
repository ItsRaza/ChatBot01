import random
import re

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
    "Ziada shaloo paloo hony ka zrort nai ha": "he he. mazak tha..",
    "Ap ne khana khaya": "Ap khana nai khata"
}

wrongQueries = [
    "Arey kehna kia chaty hoe?..",
    "I beg your pardon",
    "Ap pagal ho kia?"
]


def swap_pronouns(phrase):
    if 'Ap' in phrase:
        return re.sub('Ap', 'Ma', phrase)

    return phrase


def respond(message):
    if message in responses:
        res = random.choice(responses[message])
        swp = swap_pronouns(res)
        return swp
    else:
        return random.choice(wrongQueries)


if __name__ == "__main__":
    print("Muqaalma shuru kren..")
    message = input("USER:")
    while message != "AllahHafiz":
        print("BOT:", respond(message))
        message = input()
