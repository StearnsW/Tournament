
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

participant_spots={}
number_participants=welcome_page()
for i in range(int(number_participants)):
    participant_spots[i+1]=None
print(participant_spots)

#my_file=open('Tournament.csv','w')