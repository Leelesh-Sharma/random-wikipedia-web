import wikipedia

while True:
    random = wikipedia.random(1)
    search = input(f'Do you want to learn about the {random}. (Y/N/Q)').lower()
    if search =='q':
        break
    if search == 'n':
        continue
    elif search == 'y':
        summary = wikipedia.summary(random, sentences=5)
        print(summary+"\n")
    else:
        continue

print('QUIT.')