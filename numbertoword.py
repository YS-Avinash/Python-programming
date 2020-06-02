def integer_to_english(number):
    ones={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    digit2={'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
    tens={'10':'ten','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
    res=None
    if(len(number)==1):
        if number in ones:
            res=ones.get(number)
    elif(len(number)==2):
        if(number[-1]=='0'):
            res=tens.get(number)
        else:
            res=digit2.get(number)
    elif(len(number)==3):
        if(number[-1]=='0') and (number[-2]=='0'):
            if number[0] in ones:
                j=ones.get(number[0])#j=ones.get(number)
                res=j+' hundred'
        elif(number[1]=='0' and number[-1]!='0'):
                if number[0] in ones:
                    y=ones.get(number)
                    if number[-1] in ones:
                      f=ones.get(number[-1])
                    res=y+' hundred'+' and'+f
        elif number[-2:] in tens:
            y=tens.get(number[-2]+number[-1])
            if number[0] in ones:
                f=ones.get(number[0])
            res=f+' hundred'+' and '+y
        elif(number[-2]+number[-1]) in digit2:
            y=digit2.get(number[-2]+number[-1])
            if number[0] in ones:
                f=ones.get(number[0])
                res=f+' hundred'+' and '+y
        else:
            y=ones.get(number[0])
            f=number[1]+'0'
            h=tens.get(f)
            l=ones.get(number[-1])
            res=y+' hundred'+' and '+h+' '+l
    elif(number=='1000'):
        res='one'+' '+'thousand'
    else:
        res=-1
    return res


number=input("Enter a number:")
print(integer_to_english(number))
