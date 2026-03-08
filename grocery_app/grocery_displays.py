class grocery_display:
    def __init__(self):
        self.itemdata = ""
        self.id = ""
        self.name = ""
        self.type = ""
        self.category = ""
        self.pricetype = ""
        self.cost = 0
        self.discount = 0
        self.weight = 0
        self.show_discount = False
        self.show_weight = False
    
    # Retrieve all data fields from the selected product, converts them into dictionaries

    # Format: ID, Name, Type, Category, Price Type, Discount, Weight (discount and weight are optional)
    # Example: 00003,Sweet Solanato Tomato Punnet 200g,Tomato,Fruit,1KG,3.00,0,200

    def get_item(self, product): # "product" is retrieved from a dictionary
        self.itemdata = product # Stores full dictionary, then each variable separately
        self.id = self.itemdata["id"]
        self.name = self.itemdata["name"]
        self.type = self.itemdata["type"]
        self.category = self.itemdata["category"]
        self.pricetype = self.itemdata["pricetype"]
        self.cost = self.itemdata["cost"]
        self.discount = self.itemdata["discount"]
        self.weight = self.itemdata["weight"]
        self.show_discount = self.itemdata["show_discount"]
        self.show_weight = self.itemdata["show_weight"]
    
    def retrieve_product(self):
       return self.itemdata
    
    def display_pieces(self):
        viewedprod = self.itemdata
        format_price = lambda price : f"${price:.2f}"
        converted_price = 0
        discountedprice = float(viewedprod["id"]) - float(viewedprod["discount"])
        if viewedprod["discount"] > 0:
         display_discount = f" (was {format_price(viewedprod["cost"])}, save {format_price(viewedprod["discount"])})"
        else:
         display_discount = "" 

        price_conversion = lambda final_grams : (viewedprod["cost"] / viewedprod["weight"]) * final_grams

        if viewedprod["pricetype"] == "100G":
         converted_price = price_conversion(100)
        if viewedprod["pricetype"] == "1KG":
         converted_price = price_conversion(1000)
        if converted_price > 0:
         display_converted_price = f"\n({format_price(converted_price)} / {viewedprod["pricetype"]})"
        else:
          display_converted_price = ""
          converted_price = discountedprice
     
        return {"id_name": f"{viewedprod['id']}: {viewedprod['name']}",
                "view_stats": f"\nCategory: {viewedprod['category']} ({viewedprod['type']})\nPrice: {format_price(discountedprice)}{display_discount}{display_converted_price}",
                "menu_stats": f"- {format_price(discountedprice)} ({format_price(converted_price)} / {viewedprod['pricetype']})"}
     
    def display_item(self):
        displayparts = self.display_pieces()
        return f"{displayparts['id_name']} {displayparts['menu_stats']}"

class style_display(grocery_display):

    def __init__(self):
     super().__init__()

    def display_item(self):
        displayparts = self.display_pieces()
        return f"{displayparts['id_name']} {displayparts['view_stats']}"