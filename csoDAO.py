# carDAO.py	Data Access Object program to interact with a cso.ie API database 
			#>makes connection to the cso.ie api database
			#>downloads and formats the data.

import requests
import json

url_beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end =   "/JSON-stat/2.0/en"
        # got api from https://data.cso.ie/    datasets "TEM20" New Private Cars Licensed for the First Time 

def getAllAsFile(dataset):
        with open("carReg.json", "wt") as fp:
            print(json.dumps(getAll(dataset)), file=fp)   ##json.dumps converts file to json, easier to read. 
                                                    ## open .json file and press [alt--shift--F]
def getAll(dataset):
    url = url_beginning + dataset + url_end
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
     with open("formattedCarReg.json", "wt") as fp:
            print(json.dumps(getFormatted(dataset)), file=fp)

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {}
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}
        #print(label0)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            result[label0][label1]={}
            #print("\t",label1)
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2]=values[valuecount]
                #print("\t\t",label, " ", values[valuecount])
                valuecount+=1


    return result

# function to search for the car with the highest count for a given year and month
def findCar(year, month):
    getFormattedAsFile("TEM20")         #call the function to save the formatted data to a file
    with open('formattedCarReg.json', 'r') as file: # load the JSON data from the formatted file
        data = json.load(file)         # done this way because code is adapted from sample code in th lectures.

    year_month = f"{year} {month}"      #combine month and year into f string #https://www.programiz.com/python-programming/methods/string/format
    if year_month in data['New Private Cars Licensed for the First Time']: #check if the month and year data exists
        
        car_data = data['New Private Cars Licensed for the First Time'][year_month] #get car counts for year and month
        car_data.pop('Other', None) ; car_data.pop('All models', None) #remove 'Other' and 'All models' from the list
        new_car_data = {key: value for key, value in car_data.items() if value is not None} #filter out None values from the dictionary

        if new_car_data:
            max_count = max(new_car_data, key=new_car_data.get) #find the car with the highest count number
            return max_count
    return f"Sorry, no data was found for {month} {year}. Try a different search!" # if data is not found

if __name__ == "__main__":
    year = "2022"
    month = "September"
    result = findCar(year, month)
    print(f"Test: {month} {year} is {result}")

##https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/TEM20/JSON-stat/2.0/en
##Acknowledgment to Lecturer: Andrew Beatty for guidance through the 23-24: DATA REPRESENTATION module.