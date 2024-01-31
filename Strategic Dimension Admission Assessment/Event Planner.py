from datetime import datetime

Ourevents = []

def add_event(title, description, date, time):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M')
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return
    
    Ourevents.append({     #where we are able to enter event details
        'title': title,
        'description': description,
        'date': date,
        'time': time
    })
    print("Event added successfully.")

def list_events():
    if not Ourevents:
        print("No events found.")
        return
    
    sorted_events = sorted(Ourevents, key=lambda x: (x['date'], x['time']))
    for Ourevents in sorted_events:
        print(f"Title: {Ourevents['title']}")
        print(f"Description: {Ourevents['description']}")
        print(f"Date: {Ourevents['date']}")
        print(f"Time: {Ourevents['time']}")
        print()

def delete_event(title):
    global Ourevents
    Ourevents = [Ourevents for Ourevents in Ourevents if Ourevents['title'] != title]
    print(f"Event '{title}' deleted successfully.")

def main():
    while True:
        print("\nEvent Scheduler Menu:")
        print("1. Add your Event please")
        print("2. View your Events please")
        print("3. Delete your Event please")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':   #an option made to  enter the event details
            title = input("Enter your event title: ")
            description = input("Enter your event description: ")
            date = input("Enter your event date (YYYY-MM-DD): ")
            time = input("Enter your event time (HH:MM): ")
            add_event(title, description, date, time) #we are able to add events using the variables and function listed
        elif choice == '2':     #an option for listing 
            list_events()       #allows the option to list all the events added by using the title given for the event
        elif choice == '3':     #an option for deleting
            title = input("Enter the title of your event you wantto delete: ")
            delete_event(title)  #allows us to delete the event by our title
        elif choice == '4':     #an option for exiting
            print("Exiting...") #we are able to exit the application
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()




















