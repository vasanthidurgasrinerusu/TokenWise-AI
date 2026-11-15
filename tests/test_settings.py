from config.settings import Settings


def main():

    try:
        Settings.validate()

        print("Configuration loaded successfully!")
        print("Groq API key: Found")
        print("Groq model:", Settings.GROQ_MODEL)

    except ValueError as error:
        print("Configuration Error:", error)


if __name__ == "__main__":
    main()