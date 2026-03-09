import grocery_globalfunctions as grocery
import grocery_displays as displays

pagesize = 50
totalcost = 0

# Read file before importing, use separator
productlist = grocery.importlist("groceries.txt", ",")

# Import the contents of the file line by line, separated by the separator symbol
# productlist stores each line imported as dictionaries
shopdisplay = displays.grocery_display()
styledisplay = displays.style_display()

# Cart is stored globally
cart = []

# Search script
def searchbyid(reflist, askmessage):
   askingforid = True
   while askingforid == True: # Loops until valid ID is found
     searchitem = input(askmessage)
     filteredlist = [item for item in reflist if item["id"] == searchitem] # Only includes items with the specified ID
     try: # Only breaks loop and returns if there is at least one ID that is valid
      styledisplay.get_item(filteredlist[0]) # Since IDs are unique, it is certain that only one will be accessed
      askingforid = False
     except: # Error message if ID is not found. Used to prevent errors resulting from invalid ID
      print("Sorry, we don't have a product with this ID. Try again.")
   return styledisplay.retrieve_product() # Retrieves the dictionary


# Instructions for commands
print(f"Commands:\n* menu - View a page from the full product menu.\n* search - Search products that match the specified name or tag.\n* view - View information from a specific product.\n* cart - Order items for your cart. \n* exit - Exit the program.")

# Looping command that takes user inputs
userinput = ""
while userinput != exit:
 userinput = input("Input command: ")
 if userinput == "exit": # Used to end program
   
   # Close the program
   break
 
 if userinput == "menu":
   
   ## Displays a page from the product menu ##
   menupage = grocery.menupage(productlist, pagesize)
   for item in menupage:
     shopdisplay.get_item(item)
     print(shopdisplay.display_item())
   if len(menupage) < 1:
     print("No items beyond this page!")

 if userinput == "view":
   
   ## Search item based on ID ##
   viewed_product = searchbyid(productlist, "Enter the ID of the product you want to view: ")
   styledisplay.get_item(viewed_product)
   print(styledisplay.display_item())

 if userinput == "search":
   ## Retrieves items that fit a keyword ##

   keyword = input("Search for a keyword: ")
   searchresults = grocery.searchlist(productlist, keyword)
   if not True in searchresults: # Only shows results if True (successful match) is found
     print("No results found.")
   else:
    for item in range(len(searchresults)):
     if searchresults[item] == True:
        currentitem = productlist[item]
        shopdisplay.get_item(currentitem)
        print(shopdisplay.display_item())

 if userinput == "cart":
   cartproduct = ""
   ## Add or remove items from your cart ##
   print("* view: See the contents of your cart.\n* add: Add an item.\n* rem: Remove an item.\n* back: Return to main menu.")
   while userinput != "back":
    userinput = input("Enter a command to manage your cart: ")

    if userinput == "back" or userinput == "exit":
      break
    
    if userinput == "add":
     cartinput = (searchbyid(productlist, "Enter the ID of the item you want to add. "))
     print("Added product:", cartinput["name"])
     cart.append(cartinput)
     
    if userinput == "rem":
     if len(cart) < 1:
       print("Your cart is already empty.")
     else:
       cartinput = (searchbyid(productlist, "Enter the ID of the item you want to remove. "))
       cartremoveposition = 0
       cartremovefound = False

       for cartitem in cart:
         if cartitem["id"] == cartinput and cartremovefound == False:
          cartremoveposition = cart.index(cartitem)
          cartremovefound = True
       if cartremovefound == True:
         print("Item removed successfully.")
         cart.pop(cartremoveposition)
       else:
         print("That item is not in your cart.")

    if userinput == "view":
      format_price = lambda price : f"${price:.2f}"
      totalcost = 0
      for cartitem in cart:
        shopdisplay.get_item(cartitem)
        print(shopdisplay.display_item())
        totalcost += (cartitem["cost"] - cartitem["discount"])
        print(totalcost)
      print("Total product cost:", format_price(totalcost))
