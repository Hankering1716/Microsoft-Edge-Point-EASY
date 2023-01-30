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

for i in range(2):
    word = random.choice(words)
    browser.open(f"https://www.bing.com/search?q={word}&cvid=f930075a9e794d9fbedccf25fe597481&aqs=edge.0.69i59l4j0l2j69i60l3.1169j0j1&pglt=41&FORM=ANNTA1&PC=U531")
