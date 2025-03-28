sorry_message = "Sorry, I only tell jokes."
def main():
    user_input= input("What do you want?").lower()
    if user_input == "joke":
        print("Why did the math book look sad?")
        new_input = input("Do you want to know why?")
        print("Because it had too many problems.😂😂")
    else:
        print(sorry_message)

if __name__ == "__main__":
    main()