
def ascii_encoding_of_all_chars_word_by_word_in_sentence( sentence ):

    # split sentence into words
    word_list = sentence.split(' ')
    
    # translate each letter into ascii character
    
    i=0
    # Iterating word by word
    while i < len (word_list):
    
        res_str=''
        
        for x in word_list[i]:
        
            res_str = res_str + ord(x) #ord converts any letter to its ascii number equivalent
                                       #chr converts a number to its ascii euivalent letter
                                       
        res_str = res_str + ' '
        
        i+=1
        
    return (res_str[:-1]) #returning the whole sentence encoded as ascii values and leaving the last space
