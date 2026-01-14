# db/repl.py

from db.database import Database
from db.engine import Engine


def main():
    print("Welcome to MiniDB 🚀")
    print("Type 'exit' or 'quit' to leave.\n")

    db = Database("repl_db")
    engine = Engine(db)

    while True:
        try:
            command = input("db > ").strip()

            if not command:
                continue

            if command.lower() in ("exit", "quit"):
                print("Goodbye 👋")
                break

            result = engine.execute(command)

            if result is not None:
                print(result)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
