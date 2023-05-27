init:

    #characters
    define p = Character("You")
    define s = Character("Sophia",
                    color="#FF0000",
                    image="sophia.png")
    define b = Character("Brian",
                    color="#6495ED",
                    image="sophia.png")
    define w = Character("Dr. Wolfe",
                    color="#808080",
                    image="wolfe.png")                        

label start:

$ saysFeels = False

scene black with dissolve

"You feel a science-y explosion."
#insert time rift animation

jump part_1

label part_1:

scene bg apt with dissolve

"You wake up in a time loop.  What do you do?"

menu:

    "Go back to bed":
        jump start
    "Go to the lab":
        jump lab


label lab:

    scene bg lab with dissolve

    show wolfe at left with dissolve
    show sophia at right with dissolve
    "You see your co-workers"

    #show bryan at c
    #show sophia at right

    menu:
        "Talk to Dr. Wolfe":
            hide sophia with dissolve
            jump wolfe_greeting
    # "Talk to Bryan":
        # jump bryan_greeting
        "Talk to Sophia":
            hide wolfe with dissolve
            jump sophia_greeting
        "Sit around.":
            jump start

label wolfe_greeting:

    show wolfe at center with dissolve

    p "Hello, Dr. Wolfe."
    w "What do you want? This experiment is important to humanity, the shareholders, and my bank account. Don't fuck it up."
    p "But it leads to a time loop."
    w "I've heard that joke before. It's still not funny."

    menu:
        "'No, I'm serious. Technical jargon.'":
            w "My god, you're right. We have to stop it."
            p "Someone will have to sacrifice themself to manually shutdown the collider after the blast doors are closed."
            w "You stay here and close the doors. This was my idea. It should be me to shut it down."
            jump end_wolfe
        "'Nevermind.'":
            jump lab

label sophia_greeting:

    show sophia at center with dissolve

    s "Good morning! Aren't you excited about the experiment today?"
    menu:
        "'It causes a temporal rift and now I'm stuck in a time loop, so I guess you could say I have mixed feelings.'":
            s "If that's true, you'll have plenty of time to sort those feelings out."
            menu:
                "I'd rather prevent the rift. Will you help me?":
                    s "Oh, right. Sorry."
                    jump coinflip
                "'I have sorted them out, Sophia. I love you.'":
                    $ saysFeels = True
                    s "I- I think we should talk about this after the experiment."
                    p "But the experiment is where the loop resets. Can't we talk about it now?"
                    s "I'm just, like, really busy right now. I'll help you with the time loop thing, though."
                    jump coinflip
        "'Yup.'":
            jump lab


label coinflip:
    p "One of us has to close the blast doors from the lab console and the other has to manually shut down the collider."
    s "I've been on this project for 7 years. I designed the control system. Don't man-splain how to shut down a collider."
    p "I'm sorry, I was just trying make sure everyone understands-"
    s "No, I'm sorry. I didn't mean to blow up at you. I've been spending a lot of time on Twitter. How should we decide who dies?"
    p "That's why I brought this coin. We flip it to see who dies. Call it."
    s "Heads. Wait- don't you already?"
    "You flip the coin. It lands on heads. It always lands on heads."

menu:
    "'Heads. Thank you for your sacrifice.'":
        s "I do it for Science."
        jump end_sophiaDies
    "(LIE) 'Tails. I guess this is goodbye.'":
        s "I guess so. Before we do this, I- nevermind."
        jump end_protagDies


label end_sophiaDies:

    scene bg lab
    p "Are you ready, Sophia?"
    scene bg collider
    show sophia
    s "I'm ready."
    scene bg lab
    p "The blast doors are closed. Engage the manual shut-down. I'm sorry it came to this. Thank you."
    scene bg collider
    show sophia
    s "One more thing. I love you. I've always loved you, but was too afraid to say it. I wish we had sex before this. I'm really really really good at sex. Okay, bye."
    scene bg lab
    p "Wait, what?"
    scene black with dissolve

    jump very_end

label end_wolfe:

    scene bg collider with dissolve
    show wolfe
    w "I'm ready. Close the doors."
    scene bg lab
    #blast door sfx
    p "Doors closed. It was an honor working with you, Dr. Wolfe."
    scene bg collider
    show wolfe
    w "Please, call me Sebastian."
    scene bg lab
    p "It was an honor, Sebastian. You can shut it down now."
    scene bg collider
    show wolfe
    w "..."
    w "No."



    jump start

label end_protagDies:

    scene bg lab
    show sophia
    s "Are you ready?"
    scene bg collider
    p "I'm ready."
    scene bg lab
    show sophia
    s "The blast doors are closed."
    scene bg collider
    p "Shut down engaged. Goodbye, Sophia"
    scene bg lab
    show sophia
    s "One more thing. I love you. I've always loved you. I wish we had sex before this. I'm really really really good at sex. Okay, bye."
    scene bg collider
    p "Wait, what?"

    jump very_end


label very_end:

scene black with dissolve

"You feel a science-y implosion."
#set up a mislead animation so player thinks they're looping, but don't

"The time loop is broken. But at what cost?"

    # This ends the game.

return
