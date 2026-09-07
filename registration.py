def register_attendee(events_dict , names_dict ):
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