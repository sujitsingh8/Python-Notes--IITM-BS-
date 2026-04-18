# While loop:

print("When did India get its independence (year)?")
year=int(input())

while(year!=1947): # The loop will run until the user enters 9147
    print("You got this wrong. Enter once again.")
    year=int(input())
    # These 2 statement will execute as long as the condition in the while loop is true

print("Wowwwww...You got it right! 1940")
# It will only execute if the condition in while statement gets false!

''' while works like this:
        while <condition>
            write whatever you want here
            write whatever you want here
            write whatever you want here '''
            
# Difference between if and while loop:
'''
if —>
    Only if the condition is true, then only the statements in the if block will execute.
    Example -  If it doesn't rain I will go and play.
    
while —>
    If the condition in while is true, the statements in the while loop will keep on executing
    until or unless the condition becomes false.
    Example -  while it doesn't rain I will keep playing '''