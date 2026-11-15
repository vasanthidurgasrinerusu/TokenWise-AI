
from agent.core import CodingAgent


def main():
    agent = CodingAgent()

    task = input("What coding task should I perform? ")

    agent.run(task)


if __name__ == "__main__":
    main()
