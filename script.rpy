#to do:
#Add all story branches then use conditionals to hide
#set up characterKnows to replace characterDumb flag?
#organize conversation flags by character

#230528:added bar with tardy flag
    #Changed "tookWalk" flag to "tardy"
    #Added colliderJammed flag and respective endings
#230606: added mix convo tree with repeat tracking, which is brokensz
#230608: started changing flags to snake case format and renaming for readabilitys



init:

    python:
        tardy = False 
        #$ bryanKnows = False
        #$ wolfeKnows = False
        #$ sophiaKnows = False
        bryanDumb = True
        wolfeDumb = True
        #$ wolfeKnows = False
        #$ sophiaKnows = False
        loop_aware = False
        colliderJammed = False 
        visited_bar = False
        #mix_changedmind = False
     
        #conversation options
        # format is [character]_[topic]_talk = [boolean] where "true" allows the topic to be shown/chosen
        #mix
        mix_experiment_talk = True
        mix_timeloop_talk = False
        mix_returning = False
        mix_drinks_ordered = 0
        mix_no_drink = 0
        mix_at_bar = True

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
    define a = Character("Alex",
                    color="#808080",
                    image="wolfe.png")
    define m = Character("Mix",
                    color="#808080",
                    image="mix.png")                    

label start:

label part_1:


if loop_aware:
    scene black with dissolve
    "You feel a science-y explosion."
    #insert time rift animation

$ saysFeels = False
$ tardy = False
#$ bryanKnows = False
#$ wolfeKnows = False
#$ sophiaKnows = False
$ bryanDumb = True
$ wolfeDumb = True
$ colliderJammed = False

scene bg apt with dissolve

"June 7th, 2013 6:00 AM"
"The day of the experiment."
if loop_aware:
    "Again."
    "You are in a time loop."

menu:

    "Go back to bed":
        scene black with dissolve
        $ loop_aware = True
        jump start
    "Go to the lab":
        jump lab
    "Go to the bar":      
        $ tardy = True
        jump bar
   
    #Add "Go to the Bar"

label apartment:

menu:

    "Go back to bed":
        scene black with dissolve
        $ loop_aware = True
        jump start
    "Go to the lab":
        jump lab
    "Go to the bar":      
        $ tardy = True
        jump bar

label bar:
    $ visited_bar = True
    scene bg bar with dissolve
    if mix_at_bar:
        show mix at center with dissolve
        m "Welcome back, my friend."

    menu:
        "Talk to Mix" if mix_at_bar:
            jump mix_greeting
        "Go to the lab":
            jump lab
        "Go home": 
            jump part_1
        "Sit around":  
            $ loop_aware = True
            jump part_1


label bar_return:
    menu:
        "Talk to Mix":
            jump mix_greeting
        "Go to the lab":
            jump lab
        "Go home":
            jump part_1
        "Sit around":  
            $ loop_aware = True
            jump part_1

label mix_greeting:
    if mix_returning:
        m "Change your mind?"
    m "The usual?"
    menu:
        "The usual?":
            $ mix_drinks_ordered += 1
            m "Old Fashioned, coming right up."
            #sfx glass clink
        "Yes, please.":
            $ mix_drinks_ordered += 1
            m "Old Fashioned, coming right up."
        #sfx glass clink
        "Nothing, thanks.":
            $ mix_returning = True
            $ mix_no_drink += 1
            jump mix_no_drink   
    #menu:
     #   Add time-based dialogue after clock is implemented i.e. "It's too early to drink" or w/e

label mix_drink:

    jump mix_whatsnew

label mix_nodrink:
    if mix_no_drink < 1:
        $ mix_no_drink += 1 #track order repeats for extra sass from mix
        m "Double shot of nothing, on the house."
    elif mix_no_drink = 1:
        m "Another free glass of nothing. I have to charge you for the next one."
        $ mix_no_drink += 1
    elif mix_no_drink = 2:
        $ mix_no_drink += 1
        m "Is this your new usual?"
    else:
        "Whatever."
    jump mix_whatsnew
    
    jump bar_return

label mix_whatsnew:
    m "So, what's new and exciting?"
    jump mix_convo
label mix_convo
    menu:
        "'I'm stuck in a time loop.'" if loop_aware:
            $ mix_timeloop_talk = False 
            m "Huh."
            m "You got the Lotto numbers yet? Just kidding. If I came into money, my family would come begging before the check cleared."
            jump bar
            #jump mix_timeLoop
        "'Big experiment at the lab today.'" if mix_experiment_talk:
            $ mix_experiment_talk = False
            jump mix_experiment
       # "Not much. How are you?":
            jump mix_howismix
        "Actually, I have to go.":
            m "Alright then. See you next time."
            jump bar_return

#label mix_howismix:

label mix_experiment:
    m "Running that collider? I hope it doesn't turn the planet into a black hole or something. At least not before Terrence pays off his tab. That bastard owes me six hundred bucks."
    jump mix_whatsnew

#label mix_timeLoop:

label lab:

    scene bg lab with dissolve

    if wolfeDumb:
        show wolfe at left with dissolve
    if bryanDumb:
        show bryan at center with dissolve
    show sophia at right with dissolve
     
    menu:
        "Talk to Dr. Wolfe" if wolfeDumb:
            jump wolfe_greeting
        "Talk to Bryan" if bryanDumb:
            jump bryan_greeting
        "Talk to Sophia":
            jump sophia_greeting
        "Sit around.":
            $ loop_aware = True
            jump part_1

label wolfe_greeting:
    scene bg lab
    show wolfe at center with dissolve

    if tardy:
        w "You're late. I hate that."
    w "We are on the brink of a discovery that will benefit humanity, the shareholders, and my bank account. Don't fuck it up."
   
    menu:
        "'Too late. If we don't shut down the collider, it will create a time loop." if loop_aware:
            $ wolfeDumb = False
            $ colliderJammed = True
            w "I've heard that joke before. It's still not funny."
            jump wolfe_insist     
        "'Of course.'":
            jump lab

label wolfe_insist:
    menu:
        "'I'm serious. (TECHNICAL JARGON).'":
            w "My god, you're right. We have to stop it. You stay here and close the doors. This was my idea. It should be me to shut it down."
            jump end_wolfe
        "'Nevermind.'":
            jump lab


label bryan_greeting:
    scene bg lab
    show bryan at center with dissolve

    if tardy:
        b "You're finally here! I brought you coffee. It might be a little cold. "
    else:
         b "You're here! I brought you coffee, the usual."

    b "I heard your project is using the collider today. That's so cool. I've never even seen it up close."

    menu:
        "'It is about to blow up and get me stuck in a time loop, so I'm kind of over it.'" if loop_aware:
            $ bryanDumb = False
            b "Seriously?! I have to call my pet sitter."
            p "Why?"
            jump lab
        "'Would you like to?'" if loop_aware:
            scene black with dissolve
            jump end_bryan
        "'Maybe I can give you a tour after the experiment.'":
            b "Cool!"
            jump lab
       # "'It's pretty much just a tunnel full of tubes and electrical boxes.'":
        #    b "The most powerful one ever! This experiment will make history."
         #   p "I'm sure it will, Bryan."
          #  $ bryanDumb = False
           # b "Let me fetch you a fresh coffee."
            #jump lab

label end_bryan:
    scene bg collider with dissolve
    show bryan at center
    b "Wow! This is so cool! I promise not to touch anything."
    scene bg lab
    p "Don't worry about it. In fact , you can help me with something while you're down there.'"
    scene bg collider
    show bryan at center
    b "Really? I don't think I'm qualified..."
    scene bg lab
    p "It's easy. When I say so, pull the big red lever."
    scene bg collider
    show bryan at center
    b "The one with all the warning signs?"
    scene bg lab
    p "That's the one. Get ready."
    scene bg collider
    show bryan at center
    b "I don't feel comfortable with this. I don't like being alone down here."
    scene bg lab
    p "Everyone is alone eventually, Bryan."
    "You close the blast doors."
    #add blast door sfx
    scene bg collider
    show bryan at center
    b "What? What was that sound?"
    scene bg lab
    p "Those were the blast doors, Bryan. I can't open them until you pull the lever."
    scene bg collider
    show bryan at center
    b "Help! Let me out!"
    scene bg lab
    p "Pull the lever, Bryan. Please. There is no time to waste."
    #sfx building hum
    scene bg collider
    show bryan at center
    b "I'll do it, but this is wrong. I'm going to have to tell Dr. Wolfe."
    scene bg lab
    p "Whatever you need to do, Bryan. Thanks for all the coffee."
    scene bg collider
    show bryan at center
    b "Here goes."
    if colliderJammed:
        jump end_bryanJam

    jump very_end
    
label end_bryanJam:

    b "..."
    b "It's not moving."
    scene bg lab
    p "Please, Bryan. It's too late to argue."
    b "No, I'm trying to move it. It won't budge. What's happening?"
    p "Fuck."
    # sfx rising hum 2
    $ loop_aware = True
    scene black with dissolve
    jump part_1

label sophia_greeting:
    scene bg lab
    show sophia at center with dissolve

    if tardy:
        s "You're late! Aren't you excited about the experiment today?"
    else:
        s "Good morning! Aren't you excited about the experiment today?"
    menu:
        "'It causes a temporal rift and now I'm stuck in a time loop, so I guess you could say I have mixed feelings.'" if loop_aware:
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
        if colliderJammed:
            jump end_sophiaJam
        else:
            jump end_sophiaDies
    "(LIE) 'Tails. I guess this is goodbye.'":
        s "I guess so. Before we do this, I- nevermind."
        if colliderJammed:
            jump end_protagJam
        else:
            jump end_protagDies


label end_sophiaDies:

    scene bg lab
    p "Are you ready, Sophia?"
    scene bg collider
    show sophia
    s "I'm ready."
    scene bg lab
    p "The blast doors are closed. Engage the manual shut-down. Goodbye, Sophia."
    if colliderJammed:
        jump end_sophiaJam
    scene bg collider
    show sophia
    s "One more thing. I love you. I've always loved you, but was too afraid to say it. I wish we had sex before this. I'm really really really good at sex. Okay, bye."
    scene bg lab
    p "Wait, what?"

    scene black with dissolve

    jump very_end

label end_sophiaJam:

    scene bg collider
    show sophia
    s "Huh. It smells like Dr Wolfe's cologne in here."
    scene bg lab
    p "I hate to rush you, Sophia, but the rift opens in ten seconds."
    scene bg collider
    show sophia
    s "Right. Here goes."
    s "..."
    s "It won't move. The lever is jammed."
    s "I can't stop it. I'm sorry."
    $ loop_aware = True
    jump part_1

label end_protagJam:


    scene bg lab
    show sophia
    s "Are you ready?"
    scene bg collider
    p "I'm ready."
    scene bg lab
    show sophia
    s "The blast doors are closed. Thank you for saving our future."
    scene bg collider
    p "..."
    scene bg lab
    show sophia
    s "What's wrong?"
    scene bg collider
    p "The shut down lever is jammed. I can't move it."
    scene bg lab
    show sophia at right
    show wolfe at center with dissolve
    w "I had a feeling you would try to stop the experiment."
    w "If you're wrong about the temporal rupture, you'd be costing me billions."
    scene bg collider
    p "And if I'm right?"
    scene bg lab
    show sophia at right
    show wolfe at center
    w "Then it's not my problem."
    s "You can't do this!"
    w "I already have."
    $ loop_aware = True
    scene black with dissolve

    jump part_1


label end_wolfe:

    scene bg collider with dissolve
    show wolfe
    w "I'm ready. Close the blast doors."
    scene bg lab
    #blast door sfx
    p "Blast doors closed. It was an honor working with you, Dr. Wolfe."
    scene bg collider
    show wolfe
    w "Please, call me Sebastian."
    scene bg lab
    p "It was an honor, Sebastian. You can shut it down now."
    scene bg collider
    show wolfe
    w "..."
    w "No."
    $ loop_aware = True
    
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
