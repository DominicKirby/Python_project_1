application = True
print("1: View available events, 2: Register attendees, 3: View attendee lists, 4: Search for an attendee, 5: Display event statistics, 6: Exit the application")

names_dict = {
    1: "Alice Smith",
    2: "Bob Jones",
    3: "Charlie Brown",
    4: "Diana Prince",
    5: "Ethan Hunt",
    6: "Fiona Gallagher",
    7: "George Clooney",
    8: "Hannah Abbott",
    9: "Ian Malcolm",
    10: "Julia Roberts",
    11: "Kevin Bacon",
    12: "Laura Croft",
    13: "Michael Scott",
    14: "Natalie Portman",
    15: "Oscar Isaac",
    16: "Peter Parker",
    17: "Quentin Tarantino",
    18: "Rachel Green",
    19: "Steve Rogers",
    20: "Tony Stark",
    21: "Uma Thurman",
    22: "Victor Vance",
    23: "Wanda Maximoff",
    24: "Xavier Woods",
    25: "Yara Shahidi",
    26: "Zack Snyder",
    27: "Amber Heard",
    28: "Bruce Wayne",
    29: "Clark Kent",
    30: "Damon Salvatore",
    31: "Elena Gilbert",
    32: "Frank Castle",
    33: "Grace Hopper",
    34: "Harry Potter",
    35: "Isabella Swan",
    36: "Jack Sparrow",
    37: "Karen Page",
    38: "Luke Skywalker",
    39: "Mary Jane",
    40: "Nick Fury",
    41: "Oliver Queen",
    42: "Piper Halliwell",
    43: "Quinn Fabray",
    44: "Ross Geller",
    45: "Sam Winchester",
    46: "Dean Winchester",
    47: "Barry Allen",
    48: "Arthur Pendelton",
    49: "Lois Lane",
    50: "Lex Luthor"
}

events_dict = {
    1: {
        "event_name": "python workshop",
        "max_attendees": 10,
        "attendee_ids": [1, 2, 5, 10, 13]
    },
    2: {
        "event_name": "5 a side football",
        "max_attendees": 10,
        "attendee_ids": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    },
    3: {
        "event_name": "Basketball",
        "max_attendees": 12,
        "attendee_ids": [21, 22, 23, 28, 29]
    },
    4: {
        "event_name": "yoga",
        "max_attendees": 15,
        "attendee_ids": [8, 9, 18, 33, 35]
    },
    5: {
        "event_name": "Charity fundraiser",
        "max_attendees": 50,
        "attendee_ids": [1, 3, 7, 10, 20, 30, 40, 50]
    }
}

while application:
    """
    Application to perform 6 basic tasks based on a fictional dataset
    """
    print("-" * 31)
    choice = input("Enter your choice: ")
    print("-" * 31)

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid choice from 1-6")
    else:
        choice = int(choice)

    if choice == 1:
        """
        Printing all available events with current and maximum attten
        """
        print("All available events")

        print("\nThe events offered are:")
        for event in events_dict:
            if events_dict[event]["max_attendees"] != len(events_dict[event]["attendee_ids"]):
                print(f'  - {events_dict[event]["event_name"]} with {events_dict[event]["max_attendees"] - len(events_dict[event]["attendee_ids"])} slots free.')
            if events_dict[event]["max_attendees"] == len(events_dict[event]["attendee_ids"]):
                print(f'  - {events_dict[event]["event_name"]} with no spaces available')


    if choice == 2:
        def register_attendee(events_dict, names_dict):
            """
            Registering any attendees for any event
            """
            for event_id in events_dict:
                event = events_dict[event_id]
                print(event_id, ":", event["event_name"])
            # This prints every event

            chosen_event_id = int(input("Enter the event ID to register for: "))
            event = events_dict[chosen_event_id]
            # This asks the potential attendee to pick an event and assigns that to chosen_event_ID

            if len(event["attendee_ids"]) >= event["max_attendees"]:
                print("Sorry, that event is full.")
                return
            # This makes sure the event isn't full

            attendee_id = int(input("Enter attendee ID: "))
            # Ask the user to input their ID

            if attendee_id not in names_dict:
                print("Sorry, this ID doesn't exist")
                return
            # Make sure the ID exists

            event["attendee_ids"].append(attendee_id)
            print(f"{names_dict[attendee_id]} is now registered for {event['event_name']}.")
            # Append them to the event list

        register_attendee(events_dict, names_dict)

    if choice == 3:
        def view_attendee_lists(events_dict, names_dict):
            """
            View any attendees for given events
            """
            if not events_dict:
                print("No events available.")
                return

            print("Events:")
            for event_id, event in events_dict.items():
                print(f"{event_id}. {event['event_name']}")

            choice = input("\nEnter the event number to view attendees: ")

            if not choice.isdigit() or int(choice) not in events_dict:
                print("Invalid selection.")
                return

            event = events_dict[int(choice)]
            attendee_ids = event["attendee_ids"]

            print(f"\nAttendees for {event['event_name']}:")
            if not attendee_ids:
                print("No attendees registered yet.")
                return

            for attendee_id in attendee_ids:
                name = names_dict.get(attendee_id, "Unknown attendee")
                print(f"{attendee_id}. {name}")

        view_attendee_lists(events_dict, names_dict)



    if choice == 4:
        """
        Finding individuals from the dataset and handling possible error inputs
        """
        search_name = input(
            "Enter the attendee's name: "
        ).strip().lower()

        attendee_found = False

        for attendee_id, attendee_name in names_dict.items():
            if search_name in attendee_name.lower():

                for event in events_dict.values():
                    if attendee_id in event["attendee_ids"]:
                        print("\nAttendee found!")
                        print("Name:", attendee_name)
                        print("Event:", event["event_name"].title())
                        attendee_found = True

        if attendee_found == False:
            print("Attendee not found.")

        print("")

    if choice == 5:
        """
        Statistics on all the events attendance rate and maximum attendance possible
        """
        print("Event statistics")
        print(f"\nAmount of customers: {len(names_dict)}")
        print(f"Attendees per event: ")
        for event in events_dict.values():
            print(f'  - {event["event_name"]} : {len(event["attendee_ids"])} out of {event["max_attendees"]} maximum.')

        attendance_sum = 0
        max_attendance_sum = 0

        for event in events_dict.values():
            # noinspection bad-argument-type
            attendance_sum += len(event["attendee_ids"])
            max_attendance_sum += event["max_attendees"]
        print(f"Attendance over all events is {attendance_sum} out of {max_attendance_sum} maximum.")

    if choice == 6:
        print("Application closed")
        print("-" * 31)
        application = False

