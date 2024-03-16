#story=('Once upon a time, there was a <adjective> <noun1> who  loved to <verb> <adverb>. One day, the <noun1> met a <noun2> at <place>. They became best friends and went on many adventures together collecting <plural_noun> along the way. And they lived happily ever after.')
#with open('story.txt', 'w') as F:
#F.write(story)


def madlib_input():
    # Ask the user for various words to fill in the madlib
    adjective = input("Enter an adjective: ").lower()
    noun1 = input("Enter a noun: ").lower()
    verb = input("Enter a verb: ").lower()
    adverb = input("Enter an adverb: ").lower()
    noun2= input("Enter another noun: ").lower()
    place= input("Enter a place: ").lower()
    plural_noun= input("Enter a plural noun: ").lower()
    

    # Create the madlib story with the user's input  
    madlib = f"Once upon a time, there was {adjective} {noun1} who loved to {verb} {adverb}.\nOne day, the {noun1} met a {noun2} at {place}.\n They became best friends and went on many adventures together collecting {plural_noun} along the way.\n They lived happily ever after."

    # Display the completed madlib
    print("Here's your Madlib:")
    print(madlib)







while True:
    madlib_gen= input("Hello, Welcome to the madlib generator.\n You are to type in various words to fill in the madlib.\n Are you ready? (y/n) ").lower()
    if madlib_gen=='y':
        madlib_input()
        break
    elif madlib_gen=='n':
        quit()
    else:
        print('invalid statement')
        break