def postbank():                                                                         
    print ("Welcome to PostBank, We care for you\n")                                    
    prompt=int(raw_input)
    if prompt==1:                                                                       
        cus=BankAccount()
    elif prompt==2:                                                                     
        cus=ReturnCustomer()                        
    else:                                                                               
        print ("You have pressed the wrong key, please try again")                     
        postbank()                                          
