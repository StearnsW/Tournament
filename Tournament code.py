import os.path
import csv

# first interaction page with user

num_participants=""
print("Welcome to Tournaments R Us")
print("============================")

# check to see if this is the same tournamet or a different one, loop needs to run the first time as no tournament has been pre-specified
name_conflict = True # boolean for name conflict, begins as True since not having a name is bad
edit_existing_tournament = False # boolean are we making an edit, begins as False
tournament_name=""
while name_conflict:
    tournament_name=input("What is your tournament name?  ") # get tourney name
    if os.path.exists(f'{tournament_name}.csv'): # solve name conflict
        edit_file_checked = False # boolean for conflict solving

        while not edit_file_checked: # conflict resolution loop
            tournament_updates=input('A tournament of that name exists, are these edits to the existing tournament [y/n]: ')
            if tournament_updates!='y' and tournament_updates!='n': # invalid reply
                print("That wasn't one of the options, please resond only 'y' or 'n'")
            elif tournament_updates == 'n': # not to edit existing, leave edit conflict loop
                print("Please try a different tournament name.\n")
                edit_file_checked = True
            else: # want to edit existing, leave edit conflict loop and same name loop, change edit boolean
                print("We shall edit this tournament's file.\n")
                edit_file_checked = True
                edit_existing_tournament = True
                name_conflict = False
    else: # no overlapping name, leave same name loop (will be the case with first tournament)
        name_conflict=False


if edit_existing_tournament: # if pre-existing file take participant_spots from file
    file=open(f'{tournament_name}.csv','w') # open the file to edit
    reader = csv.reader(file)
    participant_spots={rows[0]:rows[1] for rows in reader}
    num_participants=len(participant_spots)
    file.close() # close file done when done editing.
else:
    while not num_participants.isnumeric(): # ensure number of participants is a number
        num_participants=input('Enter the number of participants (using aribic numberals): ')
        if not num_participants.isnumeric():
            print("That was not recognized as a number, please try again")

        # constructing the blank sign-up sheet (participant_spots)
    participant_spots={}
    for i in range(int(num_participants)):
        participant_spots[i+1]=None

print(f'\nThere are {num_participants} participant slots ready for sign-ups.')



