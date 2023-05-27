init:

    
    $ bryanDumb = True
    
    #characters
    define p = Character("You")
    define s = Character("Sophia",
                    color="#FF0000",
                    image="sophia.png")
    define b = Character("Bryan",
                    color="#6495ED",
                    image="sophia.png")
    define w = Character("Dr. Wolfe",
                    color="#808080",
                    image="wolfe.png")                        

label start:

scene black with dissolve

"You feel a science-y explosion."
#insert time rift animation

jump part_1

label part_1:

$ saysFeels = False
$ tookWalk = False

scene bg apt with dissolve

$ bryanDumb = True

"You wake up in a time loop.  What do you do?"

menu:

    "Go back to bed":
        jump start
    "Drive to the lab":
        jump lab
    "Walk to the lab":
        $ tookWalk = True
        jump lab

label thinkFeelings:

menu:
    "You love her":
        $ love = True
    "You don't":
        $ love = False

if love:
    "Then go to her."
else:
    "She's just a friend."

    jump part_1


label lab:

    scene bg lab with dissolve

    show wolfe at left with dissolve
    if bryanDumb:
        show bryan at center with dissolve
    show sophia at right with dissolve
    if tookWalk:
        "You arrive at the lab feeling refreshed."
    
    "You see your co-workers"
    if bryanDumb:
        menu:
            "Talk to Dr. Wolfe":
                jump wolfe_greeting
            "Talk to Bryan":
                jump bryan_greeting
            "Talk to Sophia":
                jump sophia_greeting
            "Sit around.":
                jump start

    else:
        menu:
            "Talk to Dr. Wolfe":
                jump wolfe_greeting
            "Talk to Sophia":
                jump sophia_greeting
            "Sit around.":
                jump start

label wolfe_greeting:
    scene bg lab
    show wolfe at center with dissolve

    if tookWalk:
        w "You're late. I hate that."

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

label bryan_greeting:
    scene bg lab
    show bryan at center with dissolve

    if tookWalk:
        b "You're finally here! I brought you coffee. Cream and 7 sugars, just how you like it. I hope it's not too cold. I can warm it up for you."
    else:
         b "You're here! I brought you coffee. Cream and 7 sugars, just how you like it."

    b "I heard your project is using the collider today. That's pretty awesome. I've always wanted to be part of that kind of research, but I didn't have the grades. I don't mind being the coffee guy, but I wish I got to see the collider up close just once."

    menu:
        "'It is about to blow up and get me stuck in a time loop, so I'm kind of over it.'":
            b "That's crazy! Science is weird, man. Anyway, I gotta go play video games and smoke weed now. Peace."
            $ bryanDumb = False
            jump lab
        "'Funny you should say that.'":
            scene black with dissolve
            jump end_bryan

label end_bryan:
    scene bg collider with dissolve
    show bryan at center
    b "Wow! This is so cool!"
    b "Are you sure I should be here by myself?"
    scene bg lab
    p "That's the only way to get the full experience."
    scene bg collider
    show bryan at center
    b "Right on! Thank you for letting me in here. I promise not to touch anything."
    scene bg lab
    p "Don't worry about it. In fact, you can help me with something while you're down there."
    scene bg collider
    show bryan at center
    b "Um, okay. What should I do?"
    scene bg lab
    p "Do you see that big red lever with all the warnings around it?"
    scene bg collider
    show bryan at center
    b "Yeah..."
    scene bg lab
    p "When I tell you, pull the lever all the way out."
    scene bg collider
    show bryan at center
    b "I don't feel comfortable with that. I don't really want to be alone down here anymore."
    scene bg lab
    p "Everyone is alone eventually, Bryan."
    "You close the blast doors."
    #add blast door sfx
    scene bg collider
    show bryan at center
    b "What was that?"
    scene bg lab
    p "Those were the blast doors, Bryan. I can't open them until you pull the lever."
    scene bg collider
    show bryan at center
    b "What? Why? Let me out!"
    scene bg lab
    p "As soon as you pull the lever, Bryan. Please. There is no time to waste."
    scene bg collider
    show bryan at center
    b "I guess, but I don't like this. I'm going to have to tell Dr. Wolfe."
    scene bg lab
    p "Whatever you need to do, Bryan. Thanks for all the coffee."
    scene bg collider
    show bryan at center
    b "Here goes."

    jump very_end
    


label sophia_greeting:
    scene bg lab
    show sophia at center with dissolve

    if tookWalk:
        s "You're late! Aren't you excited about the experiment today?"
    else:
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
