'''python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.
Suppose the following input is supplied to the function
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.'''


def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount=0
    for val in trans_list:
        if val[0]=='D':
            net_amount+=int(val[2:])
        else:
            net_amount-=int(val[2:])
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
