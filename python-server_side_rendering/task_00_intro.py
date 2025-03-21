import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees should be a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        
        invitation = template.format(name=name, event_title=event_title, event_date=event_date, event_location=event_location)

        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            print(f"Error: {filename} already exists.")
            continue
        
        with open(filename, "w") as file:
            file.write(invitation)
        print(f"Invitation for {name} saved as {filename}")
