#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_sum_of_evens(num):
    return sum(i for i in range(2, num+1, 2))

def menu():
    print ("1. Sum of even numbers")
    print ('2. Exit program')
