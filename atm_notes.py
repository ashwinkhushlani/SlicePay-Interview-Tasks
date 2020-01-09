# Initializing global variables
min_amount = 100
max_amount = 10000
min_note = 100
max_note = 1000

# Function to take withdrawal amount input 
def input_amt():
    amount = int(input('Enter amount you want to withdraw \n'))

    # Check if the input is valid i.e it should be between 100 to 10000
    if min_amount<= amount <=max_amount:
        # If the amount is valid call the function to calculate currency notes 
        calculate_notes(amount)
    else:
        #Else take print the output msg and take input again
        print('Invalid amount. Please enter amount in range 100 to 10000')
        input_amt()

# Function to calculate currency Notes
def calculate_notes(amount):
    # Intitialising the list with the withdrawal amount
    currency_list = [amount]
   # Iterate over the list untill the last element
    i = 0
    while i < len(currency_list):
        # Check if the value at i is not a valid currency note
        if currency_list[i] > max_note or currency_list[i] < min_note:

            # If note is not valid and greater than max_note amount divide the value of note into two values 
            # one becaomes max_note and other is the balance amount

            if currency_list[i] > max_note:
                currency_list.append(max_note)
                num = currency_list[i] - currency_list[i+1]
                currency_list.append(num)
            
            # If value at i is less that 100 then backtrack and divide the last node into multiples of 100
            else:
                temp = currency_list[i - 1]
                currency_list[i-1] = min_note
                currency_list[i] = temp - currency_list[i-1] + currency_list[i]     
        else:
            pass
        i = i+1

    # Function called to print the ouput
    print_output(currency_list)

def print_output(notes):
    # Finc the count of valid currency notes and store it in a dictionary
    my_dict = {i:notes.count(i) for i in notes if min_note <= i <= max_note}
    print("Output")
    # Iterate over the dictionary to print the output
    for i in my_dict:
        print(i,"*",my_dict[i])

# Function Called to take the input amount
input_amt()