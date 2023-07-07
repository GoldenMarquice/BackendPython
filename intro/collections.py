# lists
def colors():
    colors = ['red', 'blue', 'Pink', 'PurPle', "black", "white"]
    print(colors)

    #read
    print(colors[0])
    print(colors[3])

    #add
    colors.append("grEEn")
    print(colors)

    print ("for-----------")

    # for loop 
    # x is a variable can be changed at any time 
    for x in colors:

        print(x.lower())


def numbers():
    prices = [ 123.30, 423.4, 495, 103, 234.49, 500, 167.22, 340.43, 450, 301.23, 100]

    # 1 - print all prices with a for loop
    # 2 - find the sum of all prices
    # 3 - how mant prices are over 200

    total = 0
    numbers_over_200 = 0

    for price in prices:
        if( price >200):
            numbers_over_200 += 1

    print(" The total sum is" + str(total))
    print ("There are " + str(numbers_over_200) + "prices over 200")

    # Dictionaries 

def about_me():

    me = {
            "first_name": "Marquice",
            "last_name": "Bowman",
            "age": 33,
            "email": "na@gmail.com",
            "hobbies": ['one', 'foo', 'bar']
        }
    print(me)

    #read
    print(me["first_name"])
    print(me["age"])

    #modify
    me["age"] = me ["age"] + 1

    #add
    me["preferred_color"] = 'gray'

    #read from a non existing key
    if 'invalid' in me:
        print(me["invalid"])

def products():

    products = [
    {
        'title': 'Product 1',
        'image': 'product1.jpg',
        'category': 'Category 1',
        'price': 10.99
    },
    {
        'title': 'Product 2',
        'image': 'product2.jpg',
        'category': 'Category 2',
        'price': 19.99
    },
    {
        'title': 'Product 3',
        'image': 'product3.jpg',
        'category': 'Category 1',
        'price': 15.50
    },
    {
        'title': 'Product 4',
        'image': 'product4.jpg',
        'category': 'Category 3',
        'price': 8.75
    },
    {
        'title': 'Product 5',
        'image': 'product5.jpg',
        'category': 'Category 2',
        'price': 12.99
    },
{
        'title': 'Product 6',
        'image': 'product6.jpg',
        'category': 'Category 1',
        'price': 25.00
    },
    {
        'title': 'Product 7',
        'image': 'product7.jpg',
        'category': 'Category 3',
        'price': 14.50
    },
    {
        'title': 'Product 8',
        'image': 'product8.jpg',
        'category': 'Category 2',
        'price': 9.99
    },
    {
        'title': 'Product 9',
        'image': 'product9.jpg',
        'category': 'Category 1',
        'price': 17.50
    },
    {
        'title': 'Product 10',
        'image': 'product10.jpg',
        'category': 'Category 3',
        'price': 22.99
    },
    {
        'title': 'Product 11',
        'image': 'product11.jpg',
        'category': 'Category 2',
        'price': 11.00
    },
    {
        'title': 'Product 12',
        'image': 'product12.jpg',
        'category': 'Category 1',
        'price': 19.99
    },
{
        'title': 'Product 13',
        'image': 'product13.jpg',
        'category': 'Category 3',
        'price': 6.50
    },
    {
        'title': 'Product 14',
        'image': 'product14.jpg',
        'category': 'Category 2',
        'price': 13.99
    },
    {
        'title': 'Product 15',
        'image': 'product15.jpg',
        'category': 'Category 1',
        'price': 18.50
    }
]

    # 1 - print the titles
    # 2 - how many products are in the list?
    # 3 - sum all prices
    # 4 - how many products belong to Category 1
    # 5 - which is the most expensive product
    # 6 - and the cheapest?

    for product in products:

        print(product["title"])

    products = max(products.values('price'))

    print("Maximum value:", products)

    # call functions
#colors()
#numbers()
#about_me()
products()