def input_amt():
    min_amount = 100
    max_amount = 10000
    amount = int(input('Enter amount you want to withdraw \n'))

    if min_amount<= amount <=max_amount:
        # Call function 
        calculate_notes(amount)
    else:
        print('Invalid amount. Please enter amount in range 100 to 10000')

def calculate_notes(amount):
    currency_list = [i for i in range(100,10001)]
    notes = {}
    if amount <= 1000:
        no_of_notes = 1
        currency = amount
        notes[no_of_notes] = currency

        print_output(notes)
    else:
        pass
def print_output(notes):
    print (notes)

input_amt()