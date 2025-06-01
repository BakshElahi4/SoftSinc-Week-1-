###################################################     Tasks      ###################################################

# class User:
#     def __init__(self, name, email):
#         if not name or not isinstance(name, str):
#             raise ValueError("Name must be a non-empty string.")
#         if '@' not in email:
#             raise ValueError("Invalid email address.")
        
#         self.name = name
#         self.email = email

#     def get_role(self):
#         return "User"

#     def __str__(self):
#         return f"{self.get_role()}: {self.name} ({self.email})"


# class Intern(User):
#     def __init__(self, name, email, university):
#         super().__init__(name, email)
#         if not university or not isinstance(university, str):
#             raise ValueError("University must be a non-empty string.")
#         self.university = university

#     def get_role(self):
#         return "Intern"

#     def __str__(self):
#         return f"{super().__str__()} - University: {self.university}"


# class Mentor(User):
#     def __init__(self, name, email, expertise):
#         super().__init__(name, email)
#         if not expertise or not isinstance(expertise, str):
#             raise ValueError("Expertise must be a non-empty string.")
#         self.expertise = expertise

#     def get_role(self):
#         return "Mentor"

#     def __str__(self):
#         return f"{super().__str__()} - Expertise: {self.expertise}"

# if __name__ == "__main__":
#     user1 = User("Ali", "ali@example.com")
#     intern1 = Intern("Sara", "sara@student.com", "UET Lahore")
#     mentor1 = Mentor("Zain", "zain@mentor.org", "Machine Learning")

#     print(user1)
#     print(intern1)
#     print(mentor1)




##########################################         Challenge          ##########################################################

#user.py

#from message import Message
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.inbox = []

#     def send_message(self, receiver, text, message_log):
#         msg = Message(self, receiver, text)
#         receiver.inbox.append(msg)
#         message_log.append(msg)

#     def read_inbox(self):
#         print(f"\n📥 Inbox of {self.name}:")
#         if not self.inbox:
#             print("No messages.")
#         for msg in self.inbox:
#             print(msg)

#     def __str__(self):
#         return f"User: {self.name}"

# message.py
# class Message:
#     def __init__(self, sender, receiver, text):
#         self.sender = sender
#         self.receiver = receiver
#         self.text = text

#     def __str__(self):
#         return f"{self.sender.name} → {self.receiver.name}: {self.text}"


#manager.py
# from user import User

# class Manager(User):
#     def view_all_messages(self, message_log):
#         print(f"\n All messages (visible to Manager {self.name}):")
#         if not message_log:
#             print("No messages sent yet.")
#         for msg in message_log:
#             print(msg)


# main.py
# from user import User
# from manager import Manager
# from message import Message

# def main():
#     # Global message log
#     message_log = []

#     # Users
#     alice = User("Alice")
#     bob = User("Bob")
#     manager = Manager("Mr. Khan")

#     # Simulated chat
#     alice.send_message(bob, "Hi Bob!", message_log)
#     bob.send_message(alice, "Hey Alice! How are you?", message_log)
#     bob.send_message(manager, "Project completed.", message_log)

#     # Read inbox
#     alice.read_inbox()
#     bob.read_inbox()

#     # Manager views all messages
#     manager.view_all_messages(message_log)

# if __name__ == "__main__":
#     main()
