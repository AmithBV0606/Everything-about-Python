from random import choice

capital = "Delhi"

bird = "Peacock"

flower = "Lotus"

song = "Vande Mataram"

def randomfunfact():
    funfacts = [
        "🇮🇳 India has a floating post office Located in Dal Lake, Srinagar, it's the only floating post office in the world! It operates from a houseboat and even has a philately museum inside.",
        "🧠 India is the birthplace of zero The concept of zero as a number was invented in India by the mathematician Aryabhata around the 5th century.",
        "🌶️ The world’s hottest chili is from India The Bhut Jolokia (Ghost Pepper), grown in Assam, was once certified as the hottest chili in the world by Guinness World Records.",
        "🌍 Kumbh Mela is visible from space The Kumbh Mela, a mass Hindu pilgrimage, is so massive that it can be seen from space. In 2011, it attracted over 75 million people, making it the largest human gathering on Earth.",
        "🐫 India has a temple dedicated to rats The Karni Mata Temple in Rajasthan is home to over 25,000 rats that are worshipped. They're considered sacred and are even fed by devotees."
    ]

    index = choice("01234")

    print(funfacts[int(index)])

# if __name__ == "__main__":
# randomfunfact()

if __name__ == "__main__":
    randomfunfact()