import random
import string
import webbrowser
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

for i in range(90):
  for i in range(1):
    word = random.choice(random_words(50,5))
    browser.open(f"https://www.bing.com/search?q={word}")
