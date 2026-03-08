### Database importing and parsing ###

def importlist(filepath, separator):
 productfile = open(filepath, 'r') 
 productlist = [] # Stores all products loaded into the database
 for line in productfile: 
   readline=line.strip() # Reads each line separately
   readline = readline.replace("'","")
   readline = readline.split(separator) # Character used as separator

   # Lambdas to handle true/false conditions on optional fields
   optionalfield = lambda listposition: readline[listposition] if len(readline) > listposition else 0
   showoptional = lambda checkvariable: True if checkvariable != 0 else False

   # All products are imported as dictionaries
   productdetails = { 
       "id": readline[0],
       "name": readline[1],
       "type": readline[2],
       "category": readline[3],
       "pricetype": readline[4],
       "cost": float(readline[5]),
       "discount": float(optionalfield(6)),
       "weight": int(optionalfield(7)),
       "show_discount": showoptional(optionalfield(6)),
       "show_weight": showoptional(optionalfield(7)),
          } 
   productlist.append(productdetails)
 return productlist

# Menu command: view menu pages
def menupage(ref_list, page_size):
 pageinput_allowed = False
 while pageinput_allowed == False:
  try: # Ask for page, repeat until you type an integer
   pageinput = int(input(f"Select a page to view ({page_size} items per page) "))
   pageinput_allowed = True
  except:
   print("Page must be a number, try again")
 pagesection = page_size * pageinput
 list_min = pagesection-page_size
 return ref_list[list_min:min(pagesection, len(ref_list))]

# Used for search command: checks if a key (such as name, type or category) contains a specific string
def compare_dictionary(checkedstring, keyword):
 checkedstring = checkedstring.lower()
 keyword = keyword.lower()
 return (checkedstring.lower() in keyword.lower())

# Search command: determines whether or not each product matches the searched keyword
def searchlist(ref_list, keyword, dict_position = 0, search_results = []):
    
    sample_list = list(search_results) # Creates a copy of the original list to avoid affecting the original
    search_valid = lambda attribute : compare_dictionary(searched_dict[attribute], keyword) # Lambda which allows the compare function to be easily reused

    searched_dict = ref_list[dict_position] # Retrieves the dictionary from current position
    sample_list.append(search_valid("id") or search_valid("type") or search_valid("category")) # Check if these keys match the keyword, return True or False dependently
    #print(sample_list) # Print used for debugging how list parses search
    if dict_position == len(ref_list)-1: # Checks if all list items have been checked
     return sample_list # Finishes check
    else:
     return searchlist(ref_list, keyword, dict_position+1, sample_list) # Recursively calls itself for each check, checking the next list item each time
