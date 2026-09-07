# Python_project_1
Search for an Attendee

The attendee search feature allows the user to search for a registered attendee by entering their name.

When option 4 is selected, the program:

Asks the user to enter an attendee’s name.
Converts the search text to lowercase and removes unnecessary spaces.
Searches through the names_dict dictionary.
Checks which events contain the attendee’s ID.
Displays the attendee’s name and registered event.
Displays Attendee not found if there are no matches.

The search is not case-sensitive. It also accepts partial names. For example, entering alice, Alice, or Ali can find Alice Smith.

An attendee may be registered for more than one event. If this happens, the program displays each event containing that attendee

## View available events

...

## Register Attendee function

This function allows the user to register themselves into an event by selecting it from a list and providing their details, adding them to that event's attendee list.

**How it works:**
- Displays every event in `events_dict` with its ID and name.
- Prompts the user to enter an event number.
- Validates the input and rejects non-numeric input and event numbers that don't exist, printing `Invalid selection.` instead of crashing.
- Prompts the user to enter their name.
- Generates a new unique attendee ID, adds the name to `names_dict`, and appends the new ID to the selected event's `attendee_ids` list.
- Prints a confirmation message showing the attendee's name and the event they've registered for.

**Function:**
```python
register_attendee(events_dict, names_dict)
```
Takes the shared events and names dictionaries as arguments, updates them in place, and prints a confirmation message.

**Example usage:**
```
Enter your choice: 1
Events:
1. python workshop
2. 5 a side football
3. Basketball
4. yoga
5. Charity fundraiser
Enter the event number to register for: 4
Enter your name: Fiona Gallagher
You have successfully registered Fiona Gallagher for yoga.
```

**Edge cases handled:**
- Invalid/non-existent event number → `Invalid selection.`
- Empty name entered → prompts the user to re-enter a valid name.


## View attendee lists
Lets a user select an event and see who's registered for it.

**How it works:**
- Displays every event in `events_dict` with its ID and name.
- Prompts the user to enter an event number.
- Validates the input and rejects non numeric input and event numbers that don't exist, printing `Invalid selection.` instead of crashing.
- Looks up the selected event's `attendee_ids` list and cross references each ID against `names_dict` to display attendee names.
- If the event has no attendees yet, prints `No attendees registered yet.` instead of an empty list.

**Function:**
```python
view_attendee_lists(events_dict, names_dict)
```
Takes the shared events and names dictionaries as arguments and prints the attendee list directly.

**Example usage:**
```
Enter your choice: 3

Events:
1. python workshop
2. 5 a side football
3. Basketball
4. yoga
5. Charity fundraiser

Enter the event number to view attendees: 4

Attendees for yoga:
8. Hannah Abbott
9. Ian Malcolm
18. Rachel Green
33. Grace Hopper
35. Isabella Swan
```
**Edge cases handled:**
- Invalid/non-existent event number → `Invalid selection.`
- Event exists but has zero attendees → `No attendees registered yet.`
## Search for an attendee


## Display event statistics


