
init:
    $ current_hour = 1  # Initialize the current hour variable

define s = Character("Sophia",
                    color="#c5c5c5",
                    image="sophia.png")

define w = Character("Dr. Wolfe",
                    color="#c5c5c5",
                    image="wolfe.png")

define b = Character("Bryan",
                    color="#c5c5c5",
                    image="bryan.png")


label start:
    # Display the current hour on the screen
    $ hour_text = "Current Hour: " + str(current_hour)

    # Display the UI elements with clickable options
    vbox:
        text hour_text

        textbutton "Travel":
            $ current_hour += 1  # Increment the current hour
            jump hour_1  # Jump to the appropriate hour label

        textbutton "Wait":
            $ current_hour += 1  # Increment the current hour
            jump hour_1  # Jump to the appropriate hour label

label hour_1:
    # Code for the events and dialogue in hour 1

label hour_2:
    # Code for the events and dialogue in hour 2

# Add more hour labels as needed


    s "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
