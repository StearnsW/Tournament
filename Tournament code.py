import os.path
import csv
from secrets import choice

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
            tournament_updates=input('A tournament of that name exists, are these edits to the existing tournament? [y/n]\n')
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
    for i in range(1,len(participant_spots)+1):
        if participant_spots[i]=='None':
            participant_spots[i] = None
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
    output_menu = True
    while output_menu:
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

        if int(choice)==1:
            Sign_Up()
        elif int(choice)==2:
            Cancel_Sign_Up()
        elif int(choice)==3:
            View_Participants()
        elif int(choice)==4:
            Save_Changes()
        else:
            output_menu=not Exit()

#function to add name to participant_slots
def Sign_Up():
    print("Participant Sign Up")
    print("====================")
    spot_picked = False
    sign_up_spot='a'
    while not spot_picked:
        while not sign_up_spot.isnumeric(): # ensure number of participants is a number
            sign_up_spot=input(f"Desired starting slot #[1-{len(participant_spots)}]: ")
            if not sign_up_spot.isnumeric():
                print("That was not recognized as a number, please try again")

        if int(sign_up_spot) not in range(1,len(participant_spots)+1):
            print("That is not a valid slot, please try again")
            sign_up_spot='a'
        elif participant_spots[int(sign_up_spot)]!=None:
            print("That slot is already taken, please try again")
            sign_up_spot='a'
        else:
            spot_picked = True
    sign_up_name=input("Participant Name: ")
    print(f"Success:\n {sign_up_name} is signed up in starting slot # {sign_up_spot}")
    participant_spots[int(sign_up_spot)]=sign_up_name

#function to delete name from participant_slot
def Cancel_Sign_Up():
    print("Participant Cancellation")
    print("========================")
    made_cancellation = False
    cancel_spot='a'
    while not made_cancellation: # cancellation loop, gives the option to quit without canceling
        while not cancel_spot.isnumeric():
            cancel_spot=input(f"Starting slot #[1-{len(participant_spots)}]: ")
            if not cancel_spot.isnumeric():
                print("That was not recognized as a number, please try again")
        
        if int(cancel_spot) not in range(1,len(participant_spots)+1):
            print("That is not a valid slot, please try again")
            cancel_spot='a'
        
        cancel_name=input("Participant Name: ")
        
        if participant_spots[int(cancel_spot)]!=cancel_name:
            print(f"Error:\n{cancel_name} is not in that starting slot")
            continue_cancellation=input("Would you still like to cancel? [y/n]")
            
            if continue_cancellation!='n':
                print("You have chosen to continue the cancellation process")
                cancel_spot='a'
            else:
                made_cancellation = True
        else:
            print(f"Success:\n{cancel_name} has been cancelled from starting slot #{cancel_spot}")
            participant_spots[int(cancel_spot)]=None
            made_cancellation = True


def View_Participants():
    print("View Participants")
    print("=================")
    location_picked = False
    location='a'
    while not location_picked:
        while not location.isnumeric(): # ensure number of participants is a number
            location=input(f"Starting slot #[1-{len(participant_spots)}]: ")
            if not location.isnumeric():
                print("That was not recognized as a number, please try again")
                location='a'
        if int(location) not in range(1,len(participant_spots)+1):
            print("That is not a valid slot, please try again")
            location='a'
        else:
            location_picked = True
    location=int(location)
    nearby_locations={location}
    slot_locations=set()
    for i in range(1,6):
        nearby_locations.add(location+i)
        nearby_locations.add(location-i)
    for i in range(1,len(participant_spots)+1):
        slot_locations.add(i)
    output_locations=nearby_locations.intersection(slot_locations)
    
    print("Starting Slot: Participant")
    
    for i in output_locations:
        print(f'{i}: {participant_spots[i]}')
        

def Save_Changes():
    print("Save Changes")
    print("============")
    run_save = False
    while not run_save:
        save_changes=input("Save your changes to CVS? [y/n] ")
        if save_changes!='y' and save_changes!='n': # invalid reply
            print("That wasn't one of the options, please resond only 'y' or 'n'")
        elif save_changes == 'n': # not to edit existing, leave edit conflict loop
            print("Your changes will not be saved")
            run_save = True
        else: # want to edit existing, leave edit conflict loop and same name loop, change edit boolean
            print("Your changes will be saved")
            run_save = True
            file=open(f'{tournament_name}.csv','w') # open the file to edit
            for key in participant_spots.keys():
                file.write("%i,%s\n"%(key,participant_spots[key])) # write participant_spots to csv

            file.close()


def Exit():
    want_to_exit = False
    print("Exit")
    print("=====")
    print("Any unsaved changes will be lost.")
    is_exiting = False
    while not is_exiting:
        exiting=input("Would you like to exit? [y/n]\n")
        if exiting!='y' and exiting!='n': # invalid reply
            print("That wasn't one of the options, please resond only 'y' or 'n'")
        elif exiting == 'n': # don't exit program, exit loop
            print("You will be returned to the Main Menu")
            is_exiting = True
        else: # exit loop, change want to exit to Main Menu
            print("Goodbye!")
            is_exiting = True
            want_to_exit = True
    return want_to_exit

Main_Menu()