rock = '''
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a                                               
'''

paper = ('''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88  
''')

scissor = ('''
                     88                                                       
                     ""                                                                                                                 
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
''')
import random

game_images = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor. \n"))
comp_choice = random.randint(0, 2)

try:
    print(game_images[user_choice])
except IndexError:
    print("Invalid Choice entered. You're out of Game. "
          "Computer is not playing with you. ")
else:
    print("Computer Choice: \n", game_images[comp_choice])
finally:
    if (user_choice == 0 and comp_choice == 1) \
            or (user_choice == 1 and comp_choice == 2) \
            or (user_choice == 2 and comp_choice == 0):
        print("Computer Wins!!!")
    elif (user_choice == 0 and comp_choice == 2) \
            or (user_choice == 1 and comp_choice == 0) \
            or (user_choice == 2 and comp_choice == 1):
        print("You Win!!!")
    elif user_choice == comp_choice:
        print("It's a Draw!!!")


