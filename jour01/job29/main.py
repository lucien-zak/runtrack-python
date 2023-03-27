def listNextNote(note):
    return [note, note + 1 , note + 2]

def noteCalculatorForLuke(note):
    notes = listNextNote(note)
    for testNote in notes:
        if testNote % 5 == 0:
            return testNote
    return note
    
note = input("Entrez une note : ")
note = int(note)
print('La note arrondie est : ' + str(noteCalculatorForLuke(note)) + '/100')