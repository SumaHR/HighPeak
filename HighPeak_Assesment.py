#Program to solve goodie-dilemma problem of HighPeak Software
gd = dict()                                                                         #Initialize a dictionary 
input_file = open('Sample_input.txt','r')                                           #Input from file Sample_input.txt

for line in input_file:                                                             #Read line from input
    if line != '\n':                                                                #Exclude the empty lines
        a = line.split(":")                                                         #Separate names of the goodies and their cost
        a[1] = a[1][1:]                                                             #Remove unwanted space in the cost string
        if a[1] != "":                                                              #Remove lines which have no value
            if a[1][-1] == "\n":                                                    #Remove the endline 
                a[1] = a[1][:-1]
            gd[a[0]] = int(a[1])                                                    #Add the name of goodies and their cost as integer to a dictionery
            
input_file.close()                                                                  #Close the input file


m = gd["Number of employees"]                                                       #Extract the number of employees
del gd["Number of employees"]                                                       #After extracted, key and value deleted


s_v = sorted(gd.values())                                                           #Sort the cost in ascending order and add to a new list

l=len(s_v)                                                                          #Number of goodies
min = s_v[-1] - s_v[0]                                                              #Initialise minimum for worst case
f=0                                                                                 #f is used to store the index of the goodie with the lowest cost
for i in range((l-m)+1):                                                            #Traverse through the costs
    k = s_v[i+(m-1)] - s_v[i]                                                       #Calculate difference between maximum and minimum
    if k<min:                                                                       #Check if difference is lowest
        min=k                                                                       #If yes, update minimum value
        f=i                                                                         #And also update f to store the index where minimum cost was found

        
output_file = open('Sample_output.txt','w')                                         #write the output to Sample_output file       
output_file.write("The goodies selected for distribution are:\n")                   
output_file.write("\n")
for i in range(f,f+m):                                                              #Traverse through the costs identified to come up with minimum difference
    for j in gd.keys():                                                             #Traverse through goodies                                                             
        if gd[j] == s_v[i]:                                                         #If costs match, goodies matched
            output_file.write(j+": ")                                               #Print the name of goodie
            output_file.write(str(gd[j]))                                           #Print the cost of goodie
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(min))                                                         #Print the difference between maximum and minimum
output_file.close()

                  
    
    
        
    
    
    
    
    


