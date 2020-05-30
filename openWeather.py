#
# Script for pulling data from OpenWeather.com API
#

import urllib.request # So we can use requests
import json           # Since we are working with JSON files
import sys

zipcode = 0

# Get user entered zip code. 
def getZipCode():
    zipIsValid = False
    while zipIsValid == False:
       
        zipCode = input("Please enter a US zipcode: ")

        # Check if zipcode = 0 to break out of the loop
        if zipCode == '0':
            sys.exit("Goodbye!")

        # Send the zipcode to be validated.
        else:
            zipIsValid = validateZipcode(zipCode)
        
    return zipCode

# Validate the zip code the user entered.  Returns T/F
def validateZipcode(zipCode):

    zipLength = int(len(zipCode))

    if zipLength != 5 or zipCode.isalpha():
        print("Invalid zip code, please try again or type 0 to exit")
        return False

    else:
        return True

# Make sure the API string is valid.  Returns T/F
def verifyApiIsValid(apiString):
    url = urllib.request.urlopen(str(apiString))
 
    if (url.getcode() != 200):
        return False
    return True

# Take user entered zip code and plug it into the API string
def createApiString(zipCode):
    
    apiAddress = (f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode},us&units=imperial&APPID=f7983d661e94f2b12f418d189c1ad031")

    return apiAddress

def printResults(data):
    # Load the web data to a variable
    jsonResponse = json.loads(data)

    # Now print out some of the information from the response
    print("Weather Information for", jsonResponse["name"])
    print("--------------------------------------")
    print("Country:", jsonResponse["sys"]["country"])
    print("Current Temp:", jsonResponse["main"]["temp"], "f")
    print("Min Temp:", jsonResponse["main"]["temp_min"], "f")
    print("Max Temp:", jsonResponse["main"]["temp_max"], "f")
    print("Skies:", jsonResponse["weather"][0]["description"])
    print("Windspeed:", jsonResponse["wind"]["speed"], "mph")

def main():

    doAnother = 'y'

    while doAnother == 'y':
        # Get the zip code
        userZipCode = getZipCode()

        if userZipCode == "exit":
            break

        # Create the API link
        apiLink = createApiString(userZipCode)

        # Verify the API string is valid
        validApi = verifyApiIsValid(apiLink)

        if validApi:
            # Open the URL and read the data from it
            webData = urllib.request.urlopen(apiLink)
            if(webData.getcode() == 200):
                data = webData.read()
                printResults(data)
    
        doAnother = input("\nDo you want to enter in another zip code? (y/n): ")
        # Need to validate the answer

    print("Thanks for checking the weather. Adios!")
    exit()
   
    




if __name__ == '__main__':
    main()
