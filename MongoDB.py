from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Параметри підключення до MongoDB (додати свій пароль)
client = MongoClient(
    "mongodb+srv://sersim33:yourpassword@atlascluster.84tmng6.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster",
    server_api=ServerApi('1')
)

db = client.book

# Create (Створення)
def create_cat():
    name = input("Введіть ім'я кота: ")
    age = int(input("Введіть вік кота: "))
    features = input("Введіть характеристики кота (розділені комами): ").split(',')

    result = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": [feature.strip() for feature in features],
        }
    )
    print(f"Inserted document with id: {result.inserted_id}")

# Read (Читання)
def read_cats():
    print("Documents in collection:")
    for doc in db.cats.find():
        print(doc)

# Update (Оновлення)
def update_cat():
    name = input("Введіть ім'я кота, яке потрібно оновити: ")
    new_age = int(input("Введіть новий вік кота: "))
    new_features = input("Введіть нові характеристики кота (розділені комами): ").split(',')

    query = {"name": name}
    update_values = {"$set": {"age": new_age, "features": [feature.strip() for feature in new_features]}}
    result = db.cats.update_one(query, update_values)
    print(f"Matched: {result.matched_count}, Modified: {result.modified_count}")

# Delete (Видалення)
def delete_cat():
    name = input("Введіть ім'я кота, яке потрібно видалити: ")
    query = {"name": name}
    result = db.cats.delete_one(query)
    print(f"Deleted: {result.deleted_count}")

# Головне меню
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового кота")
        print("2. Переглянути всіх котів")
        print("3. Оновити інформацію про кота")
        print("4. Видалити кота")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            create_cat()
        elif choice == '2':
            read_cats()
        elif choice == '3':
            update_cat()
        elif choice == '4':
            delete_cat()
        elif choice == '5':
            break
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")

if __name__ == '__main__':
    main()
