
#Here we are using stack to check if the parentheses are balanced 

#Algorithm:

#define the corresponding opening and closing brackets 
#create an empty stack to allocate
#Traverse the entire input string 
#If the current character is a opening bracket: ‘(‘ or ‘{‘ or ‘[‘, push it to the top of the stack. 
#if detect closing bracket, assign the index of myChar within the closing_brackets list to the current position
#check if the current character is a corresponding parenthesis/bracket, if matches then pop it from stack.
#return true or false as matched or unmatched, the string traversal is done. 


def matching_parentheses(InputString):
	
	#define the list of all three opening brackets
	
	opening_brackets = ['(', '{', '[']
	
	#define the list of all three closing brackets
	
	closing_brackets = [')', '}', ']']
	
	#create a stack to allocate 
	
	myStack = [] 
	
	#traverse the entire InputString using for loop to find matches 
	
	for myChar in InputString:
		
		#if detect any opening brackets while traversing the string 
		
		#push myChar which is the current character as the top of myStack
		
		if myChar in opening_brackets:
			
			myStack.append(myChar)
			
		#if detect any closing brackets while traversing the string
		
		#assign the index of myChar within the closing_brackets list to the current position
		
		elif myChar in closing_brackets:
			
			current_position = closing_brackets.index(myChar)
			
			
			#if myStack is not an empty stack, and at the current position 
			#the topmost stack character is the closing bracket's corresponding opening bracket 
			#the brackets matched, return true and pop it from stack. 
			#otherwise, unmatched closing bracket, return false. 
			
			if len(myStack) > 0 and myStack[-1] == opening_brackets[current_position]:
				
				myStack.pop()
				
			else:
			
				return False
			
			#Return true if there is only letters in the string 
			
			#Return true if the string is empty
				
	return True if not myStack else False 
	
		

myString = input("Input: ")


#Call function 

print('Output:', matching_parentheses(myString))	
