#madlib game

SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def madlib():
    adj : str = input("Enter an adjective: ")
    noun : str = input("Enter a noun: ")
    verb : str = input("Enter a verb: ")
    print(SENTENCE_START + adj + " " + noun + " " + verb + ".")
madlib()