from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import urllib2
import json


def decode(im) : 
    
  # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        pass
        
    try:
        bookInfo = getISBN(str(obj.data))  
        return [bookInfo, True]
        
    except:
        pass
        return [decodedObjects, True]    
  

def getISBN(data):
    
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
   
    user_input = str(data)
    f = urllib2.urlopen(base_api_link + user_input)
    print(base_api_link + user_input)
    text = f.read()
    
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0] 
    authors = obj["items"][0]["volumeInfo"]["authors"]
    
    # displays title, summary, author, domain, page count and language
    #~ print("\nTitle:", volume_info["volumeInfo"]["title"])
    #~ print("\nSummary:\n")
    #~ print("\nAuthor(s):", ",".join(authors))
    #~ print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    #~ print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    #~ print("\nLanguage:", volume_info["volumeInfo"]["language"])
      
    
    #~ return [volume_info, authors]
    return obj
