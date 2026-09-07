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

