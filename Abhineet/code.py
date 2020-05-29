# --------------
#Code starts here

#Function to read file
def read_file(path):
        
    #Opening of the file located in the path in 'read' mode
    file= open(path, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    #Closing of the file
    file.close()

    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file
print(sample_message)

message_1=None
message_2=None

def read_file(file_path_1, file_path_2 ):
    global message_1
    global message_2

    file= open(file_path_1, 'r')    
    message_1 =file.readline()    
    file.close()
    print(message_1)

    file= open(file_path_2, 'r')    
    message_2  =file.readline()    
    file.close()
    print(message_2)

read_file(file_path_1, file_path_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    #Returning the quotient in string format
    return str(quotient)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1, message_2)

#Printing the secret message 
print(secret_msg_1)


message_3=None

def read_file(file_path_3):
    global message_3 
   

    file= open(file_path_3, 'r')    
    message_3 =file.readline()    
    file.close()
    print(message_3)

read_file(file_path_3)


def substitute_msg(message_c):

    sub=None
    if message_c =='Red':
        sub='Army General'
        return sub

    elif message_c =='Green':
        sub='Data Scientist'
        return sub

    elif message_c =='Blue':
        sub='Marine Biologist'
        return sub
    #If-else to compare the contents of the file
        
    #Returning the substitute of the message
    
    

#Calling the function to read file
secret_msg_2=substitute_msg(message_3)

#Calling the function 'substitute_msg'
print(secret_msg_2)

#Printing the secret message

message_4 =None
message_5 =None

def read_file(file_path_4 , file_path_5 ):
    global message_4 
    global message_5 

    file= open(file_path_4, 'r')    
    message_4  =file.readline()    
    file.close()
    print(message_4 )

    file= open(file_path_5, 'r')    
    message_5   =file.readline()    
    file.close()
    print(message_5 )

read_file(file_path_4 , file_path_5)




#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list =message_d.split(" ")
    
    #Splitting the message into a list
    b_list =message_e.split(" ")
    
    #Comparing the elements from both the lists
    c_list=[]
    for words in a_list:
        if words not in b_list:
            c_list.append(words)
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)


message_6=None

def read_file(file_path_6 ):
    global message_6 
   

    file= open(file_path_6 , 'r')    
    message_6 =file.readline()    
    file.close()
    print(message_6)

read_file(file_path_6 )

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split(" ")
    
    #Creating the lambda function to identify even length words
    even_word=lambda x:len(x)%2==0 
    
    #Splitting the message into a list
    b_list=filter(even_word, a_list)
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file

secret_msg_4=extract_msg(message_6)
#Calling the function 'filter_msg'
print(secret_msg_4)

#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg=" ".join(message_parts)

# # define the path where you 
# final_path= user_data_dir + '/secret_message.txt'

# #Combine the secret message parts into a single complete secret message


# #Function to write inside a file
def write_file(secret_msg,path):

    file= open(path , 'a+')    
    file.write(secret_msg)
    file.close()
          
#     #Opening a file named 'secret_message' in 'write' mode

final_path= user_data_dir + '/secret_message.txt'
#     #Writing to the file
write_file(secret_msg, final_path)
print(secret_msg)
#     #Closing the file




