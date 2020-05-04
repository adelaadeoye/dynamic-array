
"""
Testing hashing with dictionary 
"""
#Initialize the  hash table
voted={}
def check_voted(name):
    #Check if voter has voted before in the hash table
    if voted.get(name):
        #Display a message 
        print("Get out you have vote")
    #Display message that user can vote
    else:
    #hash function 
        voted[name]= True
        print("You can vote")



check_voted("adela")