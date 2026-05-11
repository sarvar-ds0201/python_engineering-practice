class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}")


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nНабор привилегий администратора:")
        for privilege in self.privileges:
            print(f" - \t{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(['разрешено добавлять сообщения',
                                      'разрешено удалять пользователей',
                                      'разрешено банить пользователей'])



sarvar_user = User('sarvar', 'ruzmatov', 22, 'tashkent')
alex_user = User('alex', 'mike', 19, 'london')
milana_user = User('milana', 'ivanova', 20, 'russia')
admin_user = Admin('oybek', 'mansurov', 34, 'usa')


sarvar_user.greet_user()
sarvar_user.describe_user()

alex_user.greet_user()
alex_user.describe_user()

milana_user.greet_user()
milana_user.describe_user()

admin_user.greet_user()
admin_user.describe_user()
admin_user.privileges.show_privileges()

