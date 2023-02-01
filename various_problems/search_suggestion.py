from difflib import SequenceMatcher

my_dict = {"hello": 1,
           "help": 2,
           "world": 3,
           "galaxy": 4,
           "love": 5,
           "hatred": 6,
           "future": 7,
           "present": 8,
           "mother": 9,
           "father": 10,
           "brother": 11,
           "sister": 12,
           "mount": 13,
           "count": 14,
           "found": 15,
           "sound": 16,
           "treasure": 17,
           "island": 18,
           "safety": 19,
           "mountain": 20,
           "bye": 21,
           "mirror": 22,
           "expect": 23,
           "anticipate": 24,
           "winning": 25,
           "lose": 26,
           "Paris": 27,
           "London": 28,
           "Yerevan": 29,
           "Lisbon": 30,
           "laptop": 31,
           "copybook": 32,
           "current": 33,
           "default": 34,
           "goodbye": 35,
           "went": 36,
           "go": 37,
           "fight": 38,
           "friend": 39,
           "family": 40,
           "enemy": 41,
           "establish": 42,
           "warfare": 43,
           "wealth": 44,
           "instance": 45,
           "memory": 46,
           "question": 47,
           "answer": 48,
           "mathematics": 49,
           "physics": 50,
           "chemistry": 51,
           "biology": 52,
           "programming": 53,
           "python": 54,
           "currency": 55,
           "dollar": 56,
           "europe": 57,
           "dream": 58,
           "king": 59,
           "queen": 60,
           "hospital": 61,
           "medicine": 62,
           "encryption": 63,
           "decryption": 64,
           "phone": 65,
           "computer": 66,
           "university": 67,
           "function": 68,
           "change": 69,
           "local": 70,
           "global": 71,
           "word": 72,
           "object": 73,
           "subject": 74,
           "country": 75,
           "city": 76,
           "number": 77,
           "village": 78,
           "program": 79,
           "book": 80,
           "library": 81,
           "birthday": 82,
           "machine": 83,
           "learning": 84,
           "power": 85,
           "helpless": 86,
           "powerful": 87,
           "warrant": 88,
           "estimate": 89,
           "play": 90,
           "evolve": 91,
           "search": 92,
           "proper": 93,
           "on": 94,
           "in": 95,
           "and": 96,
           "after": 97,
           "before": 98,
           "now": 99,
           "forever": 100
           }

"""The program will search the word you enter in a 100 word dictionary. If it's there it will inform you,if it's not
it will give you 1,2 or 3 top suggestions that are similar to your word and are present in the dictionary! """


def suggest(user_input):
    # Variables for holding the 3 biggest percents of similarity
    sim1, sim2, sim3 = 0, 0, 0
    # Variables for holding the top 3 suggestions
    suggestion1, suggestion2, suggestion3 = "", "", ""

    if user_input in my_dict.keys():
        print(f"Found {user_input} in the dictionary!")
        print("Enter 'q' to exit")

    else:
        for key in my_dict.keys():
            sim_percent = SequenceMatcher(a=user_input, b=key).ratio()
            if sim_percent >= 0.7:
                if sim_percent > sim1:
                    sim2, sim3 = sim1, sim2
                    suggestion2, suggestion3 = suggestion1, suggestion2
                    sim1 = sim_percent
                    suggestion1 = key
                elif sim1 >= sim_percent >= sim2:
                    sim3, sim2 = sim2, sim_percent
                    suggestion3, suggestion2 = suggestion2, key
                elif sim1 >= sim_percent >= sim3 and sim_percent <= sim2:
                    sim3 = sim_percent
                    suggestion3 = key
                else:
                    continue

        if suggestion1 and suggestion2 and suggestion3:
            print(f"Maybe you meant {suggestion1} or {suggestion2} or {suggestion3}?")
        elif suggestion1 and suggestion2 and not suggestion3:
            print(f"Maybe you meant {suggestion1} or {suggestion2}?")
        elif suggestion1:
            print(f"Maybe you meant {suggestion1}?")

        if sim1 < 0.7:
            print("Couldn't find the word you entered in my dictionary.")
        print("Enter 'q' to exit.")

while True:
    search = input("Enter a word: ")
    if search == 'q':
        break
    suggest(search)
