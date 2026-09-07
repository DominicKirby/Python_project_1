



        for attendee in attendees:
            if search_name in attendee["name"].lower():
                print("Attendee found!")
                print("Name:", attendee["name"])
                print("Event:", attendee["event"])
                attendee_found = True

        if attendee_found == False:
            print("Attendee not found.")

