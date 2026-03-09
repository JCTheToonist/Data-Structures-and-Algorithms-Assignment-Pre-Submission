This program simulates a grocery store application which is able to display products along with their prices.
Note: This is a demo meant for the pre-submission stage of a school project, and is meant to be a prototype for the final version.

# Included Contents
My project consists of four files: three .py modules and one .txt file. **grocery_app.py** is the file that will run the main program, and it requires the other three files to run.

## groceries.txt
The text file which grocery_app.py will read. The script will read products line by line, formatted as the following:
```ID,Name,Type,Category,Price Type,Price,Discount,Weight```

Here are examples of this format:
* Costs $2.28, price type is 1EA\
```00002,Fresh Broccoli,Broccoli,Vegetable,1EA,2.28```

* Costs $3.00 and weighs 200g, price type is 1KG (converts to $15.00/1KG)\
```00003,Sweet Solanato Tomato Punnet 200g,Tomato,Fruit,1KG,3.00,0,200```

* Costs $2.50 and weighs 200g, discount by $0.20 (meaning price is now $2.30), price type is 1KG (converts to $15.00/1KG)\
```00007,Mushrooms Cups Loose per 200g,Mushroom,Vegetable,1KG,2.50,0.20,200```

## grocery_app.py
The main code which runs the program. It is a command-based client with several commands which allow it to access the data of products stored in its database.

- **menu**: Views all products in the database, limited to the maximum page size. You can enter a page number to view the items within that page, and all items after that will be shown in the next page. The default page size of the program is 50 items. By this example, Page 1 will display items 1-50, Page 2 will display items 51-100 and so on.
- **search**: Search for a specific keyword, then displays a filtered menu that only shows products with name, type or category matching the keyword you entered.
- **view**: Views information of a specific product based on ID. It will display the product's full details, including type and category.
- **cart**: Opens the cart, which stores items for purchase. Items can be added or removed, but this build does not include purchase.
 - **view**: View all items currently inside the cart.
 - **add**: Add an item to the cart.
 - **rem**: Remove an item from the cart.
 - **back** / **exit**: Closes the cart menu. Items in the cart will remain even if you leave the menu.
- **exit**: Closes the program.

Importing the database is done through Line 8, which contains the function that will read the file and parse it into data which is accessed through dictionaries.
You can customize the _file name_ (the name of the file) and the _separator_ (the symbol used to separate different variables when loading them)
```productlist = grocery.importlist("groceries.txt", ",")```

## grocery_displays.py
Contains the object classes grocery_display and style_display (a subclass of grocery_display). These classes store product data as dictionaries through getter and setter functions, and will display them through the display_item function. The only difference between the two classes is the output of display_item:
* grocery_display displays the basic properties of the item, like ID, name, cost and item type.
* style_display displays the item's full details, and is only used by the 'view' command.

## grocery_globalfunctions.py
Contains the functions that are used globally in the project.
