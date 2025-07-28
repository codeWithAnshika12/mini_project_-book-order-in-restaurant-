menu={
    'chai':100,
    'coffie':150,
    'pastry':200,
    'sandwich':250,
    'paneer_pizza':300,
    'momos':100,
    'chilli_potato':150,
    'spring_rolls':200,
    'noodles':150,
    'fried_rice':200,
    'cold_drink':50,
    'water_bottle':30,
    'coke':50,
    'mango_juice':70,
    'orange_juice': 70,
    'ice_cream':100,
    'salad':80,
    'soup':120,
}
print("Welcome to Girllista restaurant")
for i in menu:
    print(f'{i}  : {menu[i]}Rs')

    
Total_bill=0


item_1=input('Enter your first item')
if item_1 in menu:
    qantity=int(input('How many quantity you want to order? '))
    Total_bill=Total_bill+int(menu[item_1])*qantity
    print(f'Your {item_1} is added in your order.')

        

else :
    print(f'{item_1}  is not available in our restaurant')   


add_item=input('Do you want add more orde? yes/no')    
if add_item=='yes':
      item_2=input('Plz enter your  2nd item.....')
      if item_2 in menu:
        qantity2=int(input('How many quantity you want to order? '))
        Total_bill=Total_bill+int(menu[item_2])*qantity2
        print(f'Your {item_2} is added in your order.')

      else:
        print(f'{item_2 }is not available in our restaurant') 


        
else:
    print('Thanks for ordering. ')       



if Total_bill>0:
    print(f' Thanks for ordering! Your Total_ammount is :{Total_bill} \n please wait for few movement your order will placed on your table')

else:
    print('Thanks for visiting in our restoraunt....')
    
   
