# Python_project_1

This is a project that delivers information for a Community Event Management System with workshops, sports events, and charity 
events, on a fictional dataset in Python, there is 6 options to choose from when running the application, each as follows:
1 - viewing available events, 2 - register attendees, 3 - view attendee list, 4 - search for an attendee, 5 - general event
statistics, 6 - exit application. All created from a fictional dataset in the form of a Python dictionary. 

## View available events

When you give a choice of one, you receive the title for each of the events available as well as the current attendees and maximum
amount of attendees for each event. 

Created by calling upon the created dictionary names_dict of event title and attendee amount, and delivered in a basic understandable format.

## Register Attendee function

This function allows the user to register themselves into an event ...


## View attendee lists


## Search for an attendee
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


## Display event statistics

When you select option 5, you get delivered 5 rows of information on the following: total amount of customers in the system, 
attendance per event compared to the maximum, and total attendance across the events out of the maximum space, called from the
names_dict dictionary dictating the event and attendance rates.

