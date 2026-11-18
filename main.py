from utils.storage import load_contacts
from services.contacts import (
    show_contacts,
    add_contact,
    search_contact
)


def main():
    contacts = load_contacts()

    while True:
        print("\n========== ТЕЛЕФОННАЯ КНИГА ==========")
        print("1. Показать контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Выход")
        print("=" * 38)

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            show_contacts(contacts)

        elif choice == "2":
            add_contact(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()