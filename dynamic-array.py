class Dynamic_array:
    def __init__(self,capacity=8):
        self.count=0
        self.capacity=capacity
        self.storage=[None]*self.capacity
        
    def append(self,value):
        #check if capacity  reach
        if self.count >= self.capacity:
            self.__resize__()
        
        #add the element to the array
        self.storage[self.count]=value
        #increment count
        self.count += 1
        return
        


    def __resize__(self):
        #Double the capacity
        self.capacity= 2* self.capacity

        #Create a new storage
        new_storage= [None]*self.capacity

        #Iterate through the old storage
        for i in range(self.count):
            #Copy the from the old storage
            new_storage[i]=self.storage[i]
        
        #Make the old storage the new storage
        self.storage=new_storage

Dynamic_array.append(Dynamic_array,10)
