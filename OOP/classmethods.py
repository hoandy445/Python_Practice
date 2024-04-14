# class Employee:

#     employee_count = 0

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#         Employee.employee_count += 1

#     def display_employee(self):
#         print(
# f'''
# Name: {self.name}
# Salary: {self.salary}
# ''')
        
#     @classmethod
#     def get_employee_count(cls):
#         return cls.employee_count


# emp1 = Employee('John','50000')
# emp2 = Employee('Sally','40000')
# emp3 = Employee('Mike','70000')

# emp1.display_employee()

# print('Employee count:', Employee.get_employee_count())


# class Shape:
#     shape_count = 0

#     def __init__(self,name,*args):
#         self.name = name
#         self.sides = [arg for arg in args]

#         Shape.shape_count += 1


#     def display_shape(self):
#         print(f'''
# Shape: {self.name}
# Sides: {self.sides}
# ''')

#     @classmethod
#     def get_shape_count(cls):
#         print('Total number of shapes:',end=' ')
#         return cls.shape_count


    
# shape1 = Shape('Square', 20,20)
# shape2 = Shape('Rectangle', 20,30)

# shape1.display_shape()
# print(shape1.get_shape_count())


class OnlineStore:
    store_inventory = {}
    store_sales = 0
    store_count = 0
    item_id_counter = 1000

    def __init__(self,name):
        self.name = name
        OnlineStore.store_count += 1

    def add_item(self,item_name,price,quantity):
        # create unique item ID for each item added
        OnlineStore.item_id_counter += 1 

        # update store_inventory dictionary with item information, item_id_counter as key
        OnlineStore.store_inventory.update(
            {OnlineStore.item_id_counter:
                {'Item name':item_name,
                'Price':price,
                'Quantity':quantity} 
            })

    def sell_item(self,item_id,quantity):
        # update sales        
        price = OnlineStore.store_inventory[item_id]['Price']
        sales = price * quantity
        OnlineStore.store_sales += sales


        # update item quantity
        OnlineStore.store_inventory[item_id]['Quantity'] = OnlineStore.store_inventory[item_id]['Quantity'] - quantity

    @classmethod
    def get_inventory(cls):
        return cls.store_inventory
    
    @classmethod
    def get_total_sales(cls):
        return cls.store_sales

    @classmethod
    def get_store_count(cls):
        return cls.store_count

misfortune_seafood = OnlineStore('Misfortune Seafood')

misfortune_seafood.add_item('300/UP KING CRAB',150.00,500)
misfortune_seafood.sell_item(1001,10)
print(OnlineStore.store_sales)
print(misfortune_seafood.get_inventory())
print(misfortune_seafood.get_total_sales())
print(misfortune_seafood.get_store_count())