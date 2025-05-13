

def greet(user_id,name="Guest"):
    print(f"{user_id} Hello, {name}!")


if __name__ == "__main__":
    greet(123,"Unknown")
    greet(123)