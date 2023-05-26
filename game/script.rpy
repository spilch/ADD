init:
    $ player_location = "apartment"  # Player starts in the apartment
    $ current_hour = 1  # Initialize the current hour variable
    $ hours_late = 0  # Initialize the hours late variable

# Define characters
define s = Character("Sophia", color="#FFD700", image="sophia.png")
define w = Character("Dr. Wolfe", color="#00FFFF", image="wolfe.png")
define b = Character("Bryan", color="#FF1493", image="bryan.png")
define p = Character("You", color="#FFFFFF")

    # Define locations
define apartment = Location("Apartment", "apartment.jpg")
define lab = Location("Lab", "lab.jpg")
define collider = Location("Collider", "collider.jpg")

    # Define message variables
$ msg_sophia_hour1 = Message("Sophia", "Sophia's message for hour 1")
$ msg_wolfe_hour1 = Message("Dr. Wolfe", "Dr. Wolfe's message for hour 1")

$ msg_sophia_hour2 = Message("Sophia", "Sophia's message for hour 2")
$ msg_wolfe_hour2 = Message("Dr. Wolfe", "Dr. Wolfe's message for hour 2")
$ msg_sophia_hour2_late = Message("Sophia", "Sophia's late message for hour 2")
$ msg_wolfe_hour2_late = Message("Dr. Wolfe", "Dr. Wolfe's late message for hour 2")

$ msg_sophia_hour3 = Message("Sophia", "Sophia's message for hour 3")
$ msg_wolfe_hour3 = Message("Dr. Wolfe", "Dr. Wolfe's message for hour 3")
$ msg_sophia_hour3_late = Message("Sophia", "Sophia's late message for hour 3")
$ msg_wolfe_hour3_late = Message("Dr. Wolfe", "Dr. Wolfe's late message")


label hour_1:

    # Display time loop message
    "The time loop has begun."

    $ hours_late = 0

    # Fade from black to apartment scene
    with Fade(black, 1.0)
    scene black
    show apartment

    # Display messages from Sophia and Dr. Wolfe
    $ messages.append(Message("Sophia", "Excited about the experiment culmination!"))
    $ messages.append(Message("Dr. Wolfe", "Important reminder: no room for mistakes."))

    # Display options for player actions
    menu:
        "Check messages":
            $ hour = 1
            jump check_messages

        "Go to the lab":
            $ hour = 2
            jump hour_2

        "Go back to bed":
            jump hour_1_sleep

label hour_1_sleep:

    # Display message from Sophia expressing concern
    $ messages.append(Message("Sophia", "I'm worried about you..."))

    # Display angry message from Dr. Wolfe
    $ messages.append(Message("Dr. Wolfe", "Get to work or you'll lose your job!"))

    # Display options for player actions
    menu:
        "Go to the lab":
            $ hour = 2
            jump hour_2

        "Go back to bed":
            jump hour_1_sleep

label hour_2:

    # Check if player is late
    if hours_late > 0:
        # Display NPC remark about tardiness
        if not tardiness_remark:
            $ messages.append(Message("NPC", "You're late again!"))

    # Display options for player actions
    menu:
        "Talk to Sophia":
            $ hour = 3
            jump hour_3_sophia

        "Talk to Dr. Wolfe":
            $ hour = 3
            jump hour_3_wolfe

        "Go home":
            $ hour += 1
            jump hour_2_sleep

label hour_2_sleep:

    # Display message from Sophia expressing concern
    $ messages.append(Message("Sophia", "I'm worried about you..."))

    # Display angry message from Dr. Wolfe
    $ messages.append(Message("Dr. Wolfe", "Get to work or you'll lose your job!"))

    # Display options for player actions
    menu:
        "Go to the lab":
            $ hour = 3
            jump hour_3

        "Go back to sleep":
            jump hour_2_sleep

label hour_3:

    if current_location == "apartment":
        scene bg apartment

        "You receive a new message from Sophia."
        $ messages.append(("Sophia", "There's something strange happening. I have a feeling you might be the only one who can fix it. Please come to the lab as soon as you can."))

        "You also receive a message from Dr. Wolfe."
        $ messages.append(("Dr. Wolfe", "You are fired! If anything goes wrong, it will be entirely your fault. I will sue you for every penny you have."))

    elif current_location == "lab":
        scene bg lab


        "You arrive at the lab and see Sophia and Dr. Wolfe waiting for you."



label hour_3_lab:
    show dr_wolfe at left
    show sophia at right

    menu:
        "Talk to Sophia":
            jump hour_3_sophia

        "Talk to Dr. Wolfe":
            jump hour_3_wolfe

        "Go home":
            jump hour_3_go_home

label hour_3_sophia:

    show sophia at center
    menu:
        "We are in a time loop":
            jump hour_3_sophia_loop

        "Never mind":
            jump hour_3_lab

label hour_3_sophia_loop:
    show sophia at center
    p "We are in a time loop."

    "Sophia looks at you with disbelief."

    menu:
        "No, seriously. We are in a time loop.":
            jump hour_3_sophia_confirm

        "Never mind":
            jump hour_3_lab

label hour_3_sophia_confirm:
    show sophia at center
    "Sophia's expression changes to concern."

    s "If that's true, then we need to figure out how to break free from it."

    "She asks, 'Who should we sacrifice in the collider room?'"

    menu:
        "You":
            jump ending_sophia_sacrifice

        "Me":
            jump ending_protag_sacrifice

label ending_sophia_sacrifice:
    scene collider
    show sophia at center

    s "I'm ready. By the way, I love you. Goodbye."

    menu:
        "Push the button.":
            jump very_end

        "I can't do it.":
            jump hour_1

label ending_protag_sacrifice:
    scene collider
    p "I'm ready. Goodbye."
    scene lab
    scene lab
    show sophia at center
    s "I guess this is it then. There's something I've wanted to say for a long time. I wish I'd had the courage to say it sooner."
    s "I love you."
    scene collider
    p "Wait, what?"
    jump very_end

label hour_3_wolfe:

    "You approach Dr. Wolfe and start a conversation."

    menu:
        "We are in a time loop":
            jump hour_3_wolfe_loop

        "Never mind":
            jump hour_3_lab

label hour_3_wolfe_loop:

    p "Something went wrong. I mean, will go wrong. We're in a time loop."

    w "That's not funny."

    menu:
        "No, really. We're in a time loop. The experiment fucks up.":
            jump hour_3_wolfe_confirm

        "Never mind":
            jump hour_3_lab

label hour_3_wolfe_confirm:

    "Dr. Wolfe's expression changes to determination."

    w "Alright, I'll pretend to agree to sacrifice myself to stop the experiment. Let's see what happens."

    jump ending_wolfe

label ending_wolfe:
    scene lab
    p "Okay, push the button. It was nice knowing you."
    scene collider
    w "..."
    scene lab
    p "Dr. Wolfe? It's time now. Shut it down."
    scene collider
    w "Yeah, no. This is my thing and I'm not gonna let you stop me."
    scene lab
    p "God damn it. Here we go again."
    jump hour_1


label very_end:




    "The time loop is broken. But at what cost?"

    # This ends the game.

    return
