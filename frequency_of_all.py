""" This program gives frequency of every character in the string """

#function that prints frequency of characters in given 'string'
def frequency_counter(string):
    freq_dic = {}
    for i in string:
        if i in freq_dic:    # if character already visited increase its frequency
            freq_dic[i] += 1
        else:                # if not visited marks its frequency as 1
            freq_dic[i] = 1
            
    for key, value in freq_dic.items():  # printing loop
        print(key + " --> " + str(value))


#main execution
if __name__ == "__main__":
    frequency_counter('Python is one of the versatile language')
