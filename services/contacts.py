
from utils.storage import save_contacts


def show_contacts(contacts):
    if not contacts:
        print("Телефонная книга пуста.")
        return

    print("\n--- Список контактов ---")

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} — {contact['phone']}")

    print("-" * 25)


def add_contact(contacts):
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone
        })

        save_contacts(contacts)

        print(f"Контакт {name} успешно добавлен!")

    else:
        print("Имя и номер не могут быть пустыми.")


def search_contact(contacts):
    query = input("Введите имя для поиска: ").strip().lower()

    found = [
        contact
        for contact in contacts
        if query in contact["name"].lower()
    ]

    if found:
        print(f"\nНайдено контактов: {len(found)}")

        for contact in found:
            print(f"- {contact['name']}: {contact['phone']}")

    else:
        print("Контакт не найден.")
