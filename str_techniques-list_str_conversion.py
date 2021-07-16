
def convert_string_to_list( input_str ):

    #if input_str is just one word
    list_created_1 = list( input_str)

    #if input_str is a whole sentence
    list_created_2 = input_str.split(' ')
    
    return list_created..
    

def convert_list_to_string( input_list ):

    #if list must condense to a single word
    return ''.join( input_list )
    
    #if list is collection of words
    return ' '.join( input_list )


def endode_sentence_with_next_alphabet( input_sentence ):

    # break sentence into words
    word_list = input_sentence.split(" ")
    
    word_ind = 0
    
    encoded_sentence=[]
    
    
    # iterate through all words
    while word_ind < len(word_list):
    
        curr_word=''
        
        # corner case handling with encoding logic for each word
        for ind in word_list[word_ind]:
        
                if ind == 'Z':
                   curr_word += 'A'
                elif ind == 'z':
                   curr_word +=  'a'
                else:
                    curr_word + = chr( ord(ind)+1 )
        
        # add the word to sentence
        encoded_sentence.append(curr_word)
        
        word_ind+=1
    
    # return encoded sentence
    return ' '.join(encoded_sentence)
