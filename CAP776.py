ledger = {}

data = [
    (1, "Garlic Oil - Vegetarian Capsule 500 mg", 220),
    (2, "Water Bottle - Orange", 180),
    (3, "Brass Angle Deep - Plain, No.2", 119),
    (4, "Cereal Flip Lid Container/Storage Jar - Assorted Colour", 149),
    (5, "Creme Soft Soap - For Hands & Body", 162),
    (6, "Germ - Removal Multipurpose Wipes", 169),
    (7, "Multani Mati", 58),
    (8, "Hand Sanitizer - 70% Alcohol Base", 250),
    (9, "Biotin & Collagen Volumizing Hair Shampoo + Biotin & Collagen Hair Conditioner", 1098),
    (10, "Scrub Pad - Anti- Bacterial, Regular", 20),
    (11, "Wheat Grass Powder - Raw", 261),
    (12, "Butter Cookies Gold Collection", 600),
    (13, "Face Wash - Oil Control, Active", 110),
    (14, "Mold & Mildew Remover with Bleach", 350),
    (15, "Just Spray - Mosquito Repellent Room Spray", 200),
    (16, "Dove Plastic Soap Case - Assorted Colour", 49),
    (17, "Smooth Skin Oil - For Dry Skin", 324),
    (18, "Salted Pumpkin", 180),
    (19, "Flax Seeds - Roasted", 120),
    (20, "Organic Tofu - Soy Paneer", 85.14),
    (21, "Ceramic Barrel Brush - Colour May Vary", 525),
    (22, "Instant Noodles - Chicken Satay Flavor", 45),
    (23, "Chia Seeds", 120),
    (24, "Cleanse Green Tea - Whole Leaf Loose Tea", 75),
    (25, "Veggie Cutter", 195),
    (26, "Insulated Hot Fresh Casserole For Roti/Chapati - White", 659),
    (27, "Granola - Happy Berries", 245),
    (28, "Flaxseed - Pesticide Free", 53.9),
    (29, "Paratha Puff", 90),
    (30, "Lip Butter - Rose", 169.15),
    (31, "Fruit Power - Masala Sugarcane", 19),
    (32, "Chocobakes Choc Filled Cookies", 102),
    (33, "Amber - Deodorant Body Spray", 211.65),
    (34, "Green Tea - Tulsi Loose Leaf", 225),
    (35, "Pet Solitaire Container Set - Silver", 499),
    (36, "Dhania - Dal", 98),
    (37, "Pudina Chutney Masala", 46.75),
    (38, "Bodylicious Deodorant Spray - Mate (For Men)", 136.5),
    (39, "Sport Deo Spray - Fresh, for Men", 112.75),
    (40, "Choco Deck - Mini Delights", 160),
    (41, "Eau De Toilette - Homme Green", 427.5),
    (42, "Lemon & Tea Tree Oil Soap", 360),
    (43, "Flavoured Cream Wafer Roll - Strawberry", 275),
    (44, "Storage/Lunch Steel Container with PP Lid - Red", 109),
    (45, "Plain Green Olives", 179),
    (46, "Quinoa - Organic", 250),
    (47, "After Shave Splash - Arctic Ice", 459.62),
    (48, "Colour Catcher Sheets", 799),
    (49, "Sauce - Sweet & Sour", 245),
    (50, "Super Hot and Sweet Mango Chutney", 100),
    (51, "Pani Puri Mix Paste", 48.95),
    (52, "Peach Syrup", 850),
    (53, "Acne & Oil Control Face Wash", 80),
    (54, "Choco Deck - French Dessert Inspired Layered Bar", 56),
    (55, "Extra Fine Green Peas", 202.5),
    (56, "Soothing Cucumber Facial Scrub With Apricot Seeds", 299.4),
    (57, "Foochka", 60),
    (58, "Argan-Liquid Gold Hair Spa", 199.5),
    (59, "Baby Bed Protector - Sublimation Print, Pink", 199),
    (60, "Corporate Planner Diary With Premium PU Leather Cover With Card Holder", 399),
    (61, "Atta Chalan - Stainless Steel, Size- No.8", 149),
    (62, "Dog Supplement - Absolute Skin + Coat Tablet", 348.6),
    (63, "Peanut Butter - Creamy, Super", 209.4),
    (64, "Sugar Free Petit Beurre - The Taste of France", 35),
    (65, "Aqua Halo Rejuvenating Conditioner", 168.75),
    (66, "Ayurvedic Anti-Tan Face Pack", 269.4),
    (67, "Dog Supplement - Absolute Calcium Tablet", 339.15),
    (68, "Battery Power Kids Toothbrush - Barbie", 374.25),
    (69, "Organic Carom Seeds/Ajwain/Om Kalu", 72),
    (70, "Padded Harness - 3/4 inch, Grey Colour", 840)
]

def display_products():
    print("\nAvailable Products:")
    for index, (_, product_name, price) in enumerate(data, start=1):
        print(f"{index}. {product_name} - Price: {price}")
    print("-" * 50)

def add_customer_details():
    customer_name = input("Enter customer's name: ")
    
    while True:
        display_products()
        product_choice = int(input("Enter the product number you want to purchase: "))
        
        if 1 <= product_choice <= len(data):
            _, item, price = data[product_choice - 1]
            quantity = int(input(f"Enter the quantity for '{item}': "))
            total_price = round(price * quantity, 2)
            paid_input = input("Has the customer paid? (yes/no): ")
            paid = paid_input.lower() == 'yes'
            due_amount = 0 if paid else total_price
            
            if customer_name not in ledger:
                ledger[customer_name] = []
            
            ledger[customer_name].append({
                'item': item,
                'price': price,
                'quantity': quantity,
                'total_price': total_price,
                'paid': paid,
                'due': due_amount
            })
        else:
            print("Invalid product choice.")
        
        more_items = input("Does the customer have more items? (yes/no): ")
        if more_items.lower() != 'yes':
            break

def print_customer_details():
    customer_name = input("Enter customer's name to view details: ")
    
    if customer_name in ledger:
        print(f"\nDetails for {customer_name}:")
        for entry in ledger[customer_name]:
            print(f"  Item: {entry['item']}")
            print(f"  Price per item: {entry['price']}")
            print(f"  Quantity: {entry['quantity']}")
            print(f"  Total Price: {entry['total_price']}")
            print(f"  Paid: {'Yes' if entry['paid'] else 'No'}")
            print(f"  Due: {entry['due']}")
        print("-" * 20)
    else:
        print(f"No records found for {customer_name}.")
        print("-" * 20)

add_customer_details()  
print_customer_details()
