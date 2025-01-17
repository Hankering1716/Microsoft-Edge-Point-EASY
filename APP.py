import random
import string
import webbrowser
import os
import time

def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_words(count, length):
    return [random_word(length) for i in range(count)]

words = [f"{random_words(100,5)}"]
app = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" 
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(app))
browser = webbrowser.get("chrome")

print(len(words))

for i in range(31):
    for i in range(1):
        word = random.choice(random_words(50,5))
        browser.open(f"https://www.bing.com/search?q={word}")
      
time.sleep(7)  # "Adjust this value based on the average time it takes for the browser to
#load a search result. Use 5-10 for faster PCs/Internet or 10+ for slower ones."
os.system("taskkill /im msedge.exe /f")  # Close the browser
browser.open("https://rewards.bing.com/")
