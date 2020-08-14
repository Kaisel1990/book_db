import urllib2
import json
import textwrap
import cv2
while True:

    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    #~ user_input = input("Enter ISBN: ").strip()
    user_input = "9783596178551"
    f = urllib2.urlopen(base_api_link + user_input)
    text = f.read()
    #~ text = urllib2.urlopen(base_api_link + user_input)
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0] 
    authors = obj["items"][0]["volumeInfo"]["authors"]

    # displays title, summary, author, domain, page count and language
    print("\nTitle:", volume_info["volumeInfo"]["title"])
    print("\nSummary:\n")
    print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
    print("\nAuthor(s):", ",".join(authors))
    print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    print("\nLanguage:", volume_info["volumeInfo"]["language"])
    print("\n***")

    status_update = input("\nEnter another ISBN? y or n: ").lower().strip()

    if status_update == "n":
        print("\nThank you! Have a nice day.")
        break
