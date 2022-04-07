import os.path

# first interaction page with user
def welcome_page():
    num_participants=""
    print("Welcome to Tournaments R Us")
    print("============================")
    while not num_participants.isnumeric():
        num_participants=input('Enter the number of participants (using aribic numberals): ')
        if not num_participants.isnumeric():
            print("That was not recognized as a number, please try again")

    print(f'\nThere are {num_participants} participant slots ready for sign-ups.')
    return num_participants

# constructing the blank sign-up sheet (participant_spots)
participant_spots={}
number_participants=welcome_page()
for i in range(int(number_participants)):
    participant_spots[i+1]=None

# check to see if this is the same tournamet or a different one, loop needs to run the first time as no tournament has been pre-specified
name_conflict=True
tournament_name=""
while name_conflict:
    tournament_name=input("What is your tournament name?  ")
    if os.path.exists(f'{tournament_name}.csv'):
        edit_file_checked = False
        while not edit_file_checked:
            tournament_updates=input('A tournament of that name exists, are these edits to the existing tournament [y/n]: ')
            if tournament_updates!='y' and tournament_updates!='n':
                print("That wasn't one of the options, please resond only 'y' or 'n'")
            elif tournament_updates == 'n':
                print("Please try a different tournament name.\n")
                edit_file_checked = True
            else:
                print("We shall edit this tournament's file.\n")
                edit_file_checked = True
                name_conflict = False
            print('answered')
        print('out of edit')
    else:
        name_conflict=False

file=open(f'{tournament_name}.csv','w')
file.close()