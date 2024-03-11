import random

words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
    'compiler', 'database', 'encryption', 'firewall', 'hardware',
    'internet', 'java', 'kernel', 'malware', 'network', 'object',
    'protocol', 'query', 'router', 'security', 'token', 'url',
    'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract', 'binary',
    'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
    'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node']

hangman_stages = ["""
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]

chosenword = random.choice(words)
print(chosenword)

word_display =  ['_' for _ in chosenword ]
attempts = 6 
print("Welcome to hangman")

def display_state():
    print(f"attempts = {attempts}")
    print(hangman_stages[attempts])
    print(' '.join(word_display))
    
def display_word():
    print(' '.join(word_display))

while (attempts > 0) and '_' in word_display:
    display_state()
    guess = input("Guess a letter:").lower()
    if guess in chosenword:
        for index,letter in enumerate(chosenword):
            if (letter == guess):
                if(word_display[index] == '_'): 
                    word_display = guess

    else:
        print("Incorrect")
        attempts-=1
        
    if '_' not in word_display:
        display_state()
        print("Congratulations!!!!,You won!!")
        break
    
if attempts == 0:
    display_state()
    print("SORRY,YOU LOST.. YOUR WORD WAS:",chosenword)
    
display_word()        

    
    