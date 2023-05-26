init:

    #characters
    define s = Character("Sophia",
                    color="#FFCCCC",
                    image="sophia.png")
    define p = Character("You")

label start:

"A weird scifi explosion happens."
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
    "Break the loop":
        jump very_end

label lab:

scene bg lab with dissolve

"You see your co-workers"

show sophia

menu:

    "Talk to Sophia":
        jump sophia_greeting
    "Sit around.":
        jump start

label sophia_greeting:

    s "Good morning! Aren't you excited about the experiment today?"
    p "It causes a temporal rift and now I'm stuck in a time loop, so I guess you could say I have mixed feelings."
    s "If that's true, you'll have plenty of time to sort those feelings out."
    p "I'd rather prevent the rift. Will you help me?"
    s "Oh, right. That is a better idea. I just love science so much. What should we do?"
    p "One of us has to close the blast doors from the lab and the other has to manually shut down the collider."
    s "Won't that kill them?"
    p "Yes. That's why I brought this coin. We flip it to see who dies. Call it."
    s "Heads. Wait- do you already?"
    "You flip the coin. It lands on heads. It always lands on heads."

menu:
    "Heads. Thank you for your sacrifice.":
        s "I do it for Science."
        jump end_sophiaDies
    "Tails. I guess this is goodbye.":
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
s "One more thing. I love you. I've always loved you. I wish we had sex before this. I'm really really really good at sex. Okay, bye."
scene bg lab
p "Wait, what?"
jump very_end

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
s "One more thing. I love you. I've always loved you. I wish we had sex before this. I'm really really really good at sex. Okay, bye."
scene bg collider
p "Wait, what?"

jump very_end


label very_end:

"You see a wild sci-fi explosion, then you see it in reverse."
#set up a mislead animation so player thinks they're looping, but don't

"The time loop is broken. But at what cost?"

    # This ends the game.

return
