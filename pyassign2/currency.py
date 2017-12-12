
# coding: utf-8

# In[64]:


"""currency.py: This module provides several string parsing functions to implement a simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

__author__ = "Sun Siyuan"
__pkuid__  = "1600012120"
__email__  = "1600012120@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):                               #the primary function
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""    
    
    from urllib.request import urlopen
    U="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+amount_from
    doc = urlopen(U)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')                                                     #get a string including all the information from online
    jstr=jstr.split(":")                                                              #start to split the string and get the needed data
    k=jstr[2:3]
    k=k[0].split(",")
    k=k[0].split(" ")
    k=k[1].split('"')
    k=float(k[1])                                                                     #turn the type from str to float
    return k

def test_A():                                                                         #Unit tests for the function
    """test the answer to 'from 2.5 USD to EUR'"""
    assert(exchange('USD','EUR',"2.5")==2.0952375)
def test_B():
    """test the answer to 'from 1 USD to AED'"""
    assert(exchange('USD','AED',"1")==3.672878)
def test_C():
    """test the answer to 'from 6.66 ANG to MGA'"""
    assert(exchange('ANG','MGA',"6.66")==11029.887017837)
    
def test():                                                                            #test all
    """test all cases"""
    test_A()
    test_B()
    test_C()
    print("All tests passed")
    
def main():
    """main module
    """
    currency_from=input("The currency on hand:")
    currency_to=input("The currency to convert to:")
    amount_from=input("Amount of currency to convert:")

    test()                                                                              #run the tests
    print("The amount is:",exchange(currency_from, currency_to, amount_from))           #print the answer


if __name__ == '__main__':
    main()
    


