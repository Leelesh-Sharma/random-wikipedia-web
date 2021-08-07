import wikipedia

def random_wiki_searches():
    while True:
        random = wikipedia.random(1)
        search = input(f'Do you want to learn about the {random}. (Y/N/Q)').lower()
        if search =='q':
            print('QUIT.')
            break
        if search == 'n':
            continue
        elif search == 'y':
            summary = wikipedia.summary(random, sentences=5)
            print("\n"+summary+"\n")
        else:
            print("\nInvalid action.")
            continue
            

random_wiki_searches()