class Mehul:
    def __init__(self, keys, lowerrange, higherrange):
        self.value = self.mehulfunction(keys,lowerrange, higherrange)

    def get_key_value(self):
        return self.value

    def mehulfunction(self,keys,lowerrange, higherrange):
        if lowerrange == 0 and higherrange > 0:
            return keys%(higherrange)

if __name__ == '__main__':
    list_of_keys = [23,43,1,87]
    list_of_list_index = [None,None,None,None]
    print("Before : " + str(list_of_list_index))
    for value in list_of_keys:
        #print(Mehul(value,0,len(list_of_keys)).get_key_value())
        list_index = Mehul(value,0,len(list_of_keys)).get_key_value()
        if list_of_list_index[list_index]:
            print("Collission detected")
        else:
            list_of_list_index[list_index] = value

    print("After: " + str(list_of_list_index))