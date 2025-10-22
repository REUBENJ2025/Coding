#Libary books
#Reuben Joseph
#Greg Allcock
#21/10/25
#Computer Science

import os
import json

folder = os.path.join(os.path.expanduser("~"), "Documents", "BookData")
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, "books.json")

text_docus = os.path.join(folder, "books.txt")

def books_txt():
    with open("books.txt", "w") as file:
        file.write(str(101))
        file.write("\n")

def book_list(books):
    books = [
    [101,"Python Basics",True],
    [102,"AI Explained",False],
    [103,"Data Structures",True],
    [104,"The Code Breakers",True]

]

