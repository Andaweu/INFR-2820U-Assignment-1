
import time


def loadfile():

    productArray = []
    individualProduct = []
    text_file = open("product_data.txt", "r")
    for line in text_file:
        line = line.replace("\n", "")
        line = line.split(",")
        productArray.append(line)
    text_file.close()

    return productArray

products = loadfile()
sortedList = products

def displayList(productList):
 x=0
 for item in productList:
     x += 1
     print("{}. {}".format(x, item))


def insertItem(products):
    newItem = []
    while True:
     productID = int(input("Enter the new product ID:  "))
     newItem.append(productID)

     productName = input("Enter the product name:  ")
     newItem.append(productName)

     productPrice = float(input("Enter the products price:  "))
     newItem.append(productPrice)

     productCategory = input("Please enter the product category:  ")
     newItem.append(productCategory)

     print(newItem)

     print("Is all the product information correct? (1. Yes, 2. No)")
     print(newItem)
     correct = int(input(">>>"))
     if correct == 1:
        break
     else:
        continue
    return newItem

#products.append(insertItem())


def updateItems(productList):
    displayList(productList)
    print("Please select the item you wish to edit")
    selectedItem = int(input(">>> ")) - 1
    print()
    print(productList[selectedItem])
    print("Which element would you like to modify 1.ID 2.Name 3.Price 4.Category")
    selectedElement = int(input(">>> ")) - 1
    if selectedElement == 0:
      print("You selected product ID")
      print (productList[selectedItem][selectedElement])
      newID = int(input("Choose a new ID:  "))
      productList[selectedItem][selectedElement] = newID
    elif selectedElement == 1:
      print("You selected Product Name")
      print (productList[selectedItem][selectedElement])
      newName = input("Choose a new ID:  ")
      productList[selectedItem][selectedElement] = newName
    elif selectedElement == 2:
      print("You selected Product Price")
      print (productList[selectedItem][selectedElement])
      newPrice = input("Choose a new ID:  ")
      productList[selectedItem][selectedElement] = newPrice
    elif selectedElement == 3:
      print("You selected Product Category")
      print (productList[selectedItem][selectedElement])
      newCategory = input("Choose a new ID:  ")
      productList[selectedItem][selectedElement] = newCategory



def deleteItems(productList):
     displayList(productList)
     toBeDeleted = int(input('Select the item you wish to delete:  '))
     productList.pop(toBeDeleted-1)
     displayList(productList)


def searchItems(productList):
    displayList(productList)
    matchingResults = []
    searchCategory = int(input("Which category would you like to search for 1.ID 2.Name 3.Price 4.Category:  ")) - 1
    searchQuery = input("Search:   ")
    searchValues = len(productList) + 1
    i = 0

    while i in range(searchValues):
       
       try:
          searchedValue = productList[i][searchCategory].index(searchQuery)
          matchingResults.append(productList[i])
          i += 1
       except:
          i += 1

    for item in matchingResults:
        print(item)

    return matchingResults


'''
#displayList()
   
updateItems(products)

displayList()

searchItems(products)
'''

def sortItems(productList):
    start_time = time.time()
    listLength= len(productList)
    swapped = False

    for i in range(listLength-1):

        for j in range(0, listLength-i-1):
 

            if float(productList[j][2]) > float(productList[j + 1][2]):
                swapped = True
                productList[j], productList[j + 1] = productList[j + 1], productList[j]
         
        if not swapped:
           break

    end_time = time.time()
    total_time = end_time - start_time
    print("The total elapsed time is {} seconds".format(total_time))

    return        
 
 

 
sortItems(sortedList)
 
print("Sorted array is:")
for i in range(len(sortedList)):
    print(sortedList[i])

