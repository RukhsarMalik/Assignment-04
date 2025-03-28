adj: str = input("Enter an adjective: ")
noun: str = input("Enter a noun: ")
verb1: str = input("Enter a verb: ")
noun2: str = input("Enter another noun: ")
adj2: str = input("Enter another adjective: ")
verb2: str = input("Enter another verb with second form: ")

madlib: str = f"I saw a {adj} {noun} that tried to {verb1} my {noun2}. \
It was so {adj2} that I just {verb2} away!"

print(madlib)