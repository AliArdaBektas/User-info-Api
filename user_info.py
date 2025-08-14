import requests
import random
import webbrowser

url =f"https://dummyjson.com/users"
response = requests.get(url)
data = response.json()


def user_info():
    random_user = random.choice(data['users'])
    image = random_user['image']

    print(f"Name: {random_user['firstName']}")
    print(f"Last Name: {random_user['lastName']}")
    print(f"age: {random_user['age']}")
    print(f"Gender: {random_user['gender']}")
    print(f"Email: {random_user['email']}")
    print(f"Phone Number: {random_user['phone']}")
    print(f"User ID: {random_user['id']}")

    question1 = input("Do you wanna see the profile picture of this user(yes/no):")
    if question1 == "yes":
        print(f"Your are about to see the image")
        webbrowser.open(image)
    else:
        print("")

question2 = "yes"

while question2.lower() == "yes":
    user_info()
    question2 = input("Do you wanna take a look of another user?:")

