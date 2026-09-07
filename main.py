

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
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("\n The available events are:")
        for event in events_dict:
            if events_dict[event]["max_attendees"] != len(events_dict[event]["attendee_ids"]):
                print(f'  - {events_dict[event]["event_name"]} with {events_dict[event]["max_attendees"] - len(events_dict[event]["attendee_ids"])} slots free.')
            if events_dict[event]["max_attendees"] == len(events_dict[event]["attendee_ids"]):
                print(f'  - {events_dict[event]["event_name"]} with no spaces available')
        print("\n")


    if choice == 2:
        print(choice)

    if choice == 3:
        print(choice)

    if choice == 4:
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

    if choice == 5:
        print(choice)

    if choice == 6:
        print(choice)
        application = False

