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
    file=open(f'{tournament_name}.csv','r') # open the file to edit
    reader = csv.reader(file)
    participant_spots={int(rows[0]):rows[1] for rows in reader} # build participant_spots from csv
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

print(f'\nThere are {num_participants} participant slots ready for sign-ups.') # print number of spaces in tourney

#the main menu, returns value of where it wants to go (can be made to call methods internally later)
def Main_Menu():
    print("Participant Menu")
    print("================")
    # options
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save Changes")
    print("5. Exit")
    #loop to make sure they choose a valid option
    choice_made = False
    while not choice_made:
        choice=input("What would you like to do, please enter the corresponging number: ")
        if choice not in {'1','2','3','4','5'}:
            print("Not a recognized choice, please try agian")
        else:
            choice_made = True
    return choice

#function to add name to participant_slots
def Sign_Up():
    print("Participant Sign Up")
    print("====================")
    spot_picked = False
    while not spot_picked:
        spot=int(input(f"Desired starting slot #[1-{len(participant_spots)}]: "))
        if spot not in range(1,len(participant_spots)+1):
            print("That is not a valid spot, please try again")
        elif participant_spots[spot]!=None:
            print("That spot is already taken, please try again")
        else:
            spot_picked = True
    name=input("Participant Name: ")
    print(f"Success:\n {name} is sighed up in starting slot # {spot}")
    participant_spots[spot]=name




file=open(f'{tournament_name}.csv','w') # open the file to edit
for key in participant_spots.keys():
    file.write("%i,%s\n"%(key,participant_spots[key])) # write participant_spots to csv

file.close()

