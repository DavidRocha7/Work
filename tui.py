def display_title(title_text):
    print("-" * len(title_text))
    print(title_text)
    print("-" * len(title_text))


def input_menu_choice(prompt, valid):
    valid = [v.upper() for v in valid]
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid:
            return choice
        print(f"\nInvalid choice. Please enter one of: {', '.join(valid)}")


def main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")
    return input_menu_choice("\nYour choice: ", ["A", "B", "C", "X"])


def submenu_view_data():
    print("\n[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    return input_menu_choice("\nYour choice: ", ["A", "B", "C", "D"])


def submenu_visualise_data():
    print("\n[A] Most reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")
    return input_menu_choice("\nYour choice: ", ["A", "B", "C"])


def submenu_export_format():
    print("\n[A] TXT")
    print("[B] CSV")
    print("[C] JSON")
    return input_menu_choice("\nYour choice: ", ["A", "B", "C"])
