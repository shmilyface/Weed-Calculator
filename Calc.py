def calc():
    while True:
        try:
            G = float(input('Quantity of Grams: '))
            if G < .001 or G > 20:
                raise ValueError
                break
        except ValueError:
            print('Please choose a valid number of grams')
        break
    thc_high = 23 # assign variable values via strain selection
    thc_low = 44 # assign variable values via strain selection
    
    S = ((thc_high + thc_low)/2)
    P = 10 * (G * S)
    
    if S >= .2 and P > 0:
        print('Strain contains high THC content amount of:','{:,.0f}'.format(float(S)) + '%')
        print('Use contains a Potency Level of:','{}'.format(int(P)) + 'mg')
    elif S >= .10 or S <= .15 and P > 0:
        print('Strain contains mid-level THC content amount of:','{:,.2f}'.format(float(S)) + '%')
        print('Use contains a Potency Level of:','{}'.format(int(P)) + 'mg')
    elif S <= .05 and P > 0:
        print('Strain contains low-level THC content amount of:','{:,.0f}'.format(float(S)) + '%')
        print('Use contains a Potency Level of:','{}'.format(int(P)) + 'mg')
            