from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import urllib2
import json
import cv2

def decode(im) : 
  # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
  
    try:
        getISBN(str(obj.data))  
        return [decodedObjects, False]
    except:
        pass
        return [decodedObjects, True]    
  

def getISBN(data):
    
    print ('Suche...')
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
   
    user_input = str(data)
    
    f = urllib2.urlopen(base_api_link + user_input)
    
    text = f.read()
    
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0] 
    authors = obj["items"][0]["volumeInfo"]["authors"]
    
    # displays title, summary, author, domain, page count and language
    print("\nTitle:", volume_info["volumeInfo"]["title"])
    print("\nSummary:\n")
    print("\nAuthor(s):", ",".join(authors))
    print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    print("\nLanguage:", volume_info["volumeInfo"]["language"])
    
    print ('Ende Suche')    

# Display barcode and QR code location  
def display(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
    
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;
      
    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Display results 
  cv2.imshow("Results", im);
  #~ cv2.waitKey(0);
  
  
#~ # Main 
#~ if __name__ == '__main__':

  #~ # Read image
  
  #~ im = cv2.imread('barcode.jpg')

  #~ decodedObjects = decode(im)
  #~ display(im, decodedObjects)
