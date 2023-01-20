# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Naming convenction:   
#   c_ for Charater 
#   b_ for Backgrounds
#   m_ for Music Tracks


# Choice Flags
default Ttka_Halot_taken = False
default Sword_taken = False

default visited_Corridor = False
default visited_Library = False
default visited_Attic = False
default visited_Bedroom = False

# Characters
define narration = Character("Thoughts", color="#d85a06")
define you = Character("You", color="#638eb1")

# The game starts here.

label start:
    
    #######
    # Black
    scene bg black
    play music "Depth of Innsmounth.mp3"
    pause 1.0

    #############
    # INTRO SCENE
    "You don't exactly know how you got here. There's a void in your head."
    "But you can still remember who you are, and what you're doing here."
    "You are a game developer at a very prominent game studio, and you used your savings to take a trip with your friends to England, where you live."
    "You are all fans of horror stories and board games, and there are a couple of Narrative Designers in the group..."
    "... who, when they saw Innsmouth's name on the map, got curious."
    "They let you know that Innsmouth is the fictional name of an American town in one of Lovecraft's stories."
    play sound "Audio - creepy leaves at night.wav"
    "You were passing through anyway and the sun was setting. So you decided that spending a night in Innsmouth would be thrilling."
    "But the rest, as soon as you crossed the border of that eerie little town ... is hazy, in your memories."
    
    scene bg mansion with fade

    "You gaze at the unsettling manor house looming before you. Thin spires reaching obliquely toward the sky, with tiles blackened as if burnt out by a fire."
    "Even the gray stone of which the castle's exterior is made, it reminds one of an insane pallor, close to death."
    "All around the manor, the diseased and leafless trees seem to bend in your direction, with irregular and sinister articulations of the branches, in what seems to be an expression of grief."
    "You look around, and you realize-that you are engulfed in darkness. You see nothing behind you-but you hear the creaking of wood, the confused rustling of leaves, and more sounds you can't quite understand."
    "A chill runs through your body. Where are the others? What has happened to them? There is no sign of them, and you begin to think that you should find shelter from the darkness."
    "So you make your way to the entrance of the manor house."

    scene bg black with fade 

    play sound "Audio - door handle.wav"
    pause 0.5
    play sound "Audio - big door opening.wav"
    pause 0.5

    jump Corridor

label Corridor:
    ################
    # ENTRANCE SCENE
    scene bg corridor with fade
    if visited_Corridor == False:
        $ visited_Corridor = True
        "Nonostante le luci accese, la tua prima impressione è che questo luogo sia stato abbandonato a sé stesso."
        "L'aria di questo luogo sembra più rarefatta- come una nebbia altamente improbabile. Potrebbe essere polvere, o cenere."
        "Ti trovi in quello che sembrerebbe essere una grande entrance hall, con delle scale che portano verso l'alto."
        "Una delle stanze al piano di sopra sembra aperta, forse uno studio di qualche genere."
        "L'altra parte della scala, invece, porta direttamente all'attico."
        "Questo piano sembra portare a un lungo corridoio, difficile sapere dove potrebbe farti finire."

    menu:
        "Library":
            scene bg black with fade 
            pause 0.5
            jump Library

        "Attic":
            scene bg black with fade 
            pause 0.5
            jump Attic

        "Bedroom":
            scene bg black with fade 
            pause 0.5
            jump Bedroom
    

label Library:
    scene bg library with fade
    if visited_Library == False:
        $ visited_Library = True
        "You stand in a dusty studio. The smell of old paper and ink fills your nostrils."
        "In front of you stands a desk of fine wood, with wavy legs and a surface covered with a glass plate in which elegant decorations are carved."
        "It is impossible to decipher the decorations, for the table is almost entirely taken up by tomes haphazardly stacked on top of each other, yellowed papers, fountain pens and ink nibs."
        "The walls of the room are mostly taken up by ceiling-high bookcases with countless books and knick-knacks."
        "You look around, and your attention is caught by an artifact that, of all things, seems strange to find in a study."
        "It is a sword with rather ancient features, forged in a metal that seems alien to you and which, because of its color, you could perhaps trace back to copper."
        "The sword must be of a ceremonial type, for it is studded with decorations on the hilt, the guard and the base of the blade itself."
        "In particular, right there lies the figure of an ungodly creature you have never seen before. Its head is crowned with a ruby."

        "Do you want to take the sword?"
        menu:
            "Yes":
                $ Sword_taken = True
                play sound "Audio - item taken.wav"

            "No":
                $ Sword_taken = False

        "You walk back to the door, and in doing so you hear a thud. You accidentally dropped a book."
        "When you pick it up to put it back, you notice that it is a smoke-gray tome with a leather cover where symbols are inscribed."
        "They look like occult symbols going around a circle, and at the bottom is the title:"
        "T'tka Halot."
        "You open it. The book contains a series of hand-made illustrations, so old that the ink, formerly black, has changed color along with the yellowing of the pages."
        "You don't understand anything written in it, but they look like some sort of chants."

        "Do you want to take the T'tka Halot?"
        menu:
            "Yes":
                $ Ttka_Halot_taken = True
                play sound "Audio - item taken.wav"

            "No":
                $ Ttka_Halot_taken = False
    else:
        if Sword_taken == False:
            "Do you want to take the sword?"
            menu:
                "Yes":
                    $ Sword_taken = True
                    play sound "Audio - item taken.wav"

                "No":
                    $ Sword_taken = False
        if Ttka_Halot_taken == False:
            "Do you want to take the T'tka Halot?"
            menu:
                "Yes":
                    $ Ttka_Halot_taken = True
                    play sound "Audio - item taken.wav"

                "No":
                    $ Ttka_Halot_taken = False
    
    "There is nothing left for you to do here, and you back to the corridor."
    scene bg black with fade 
    pause 0.5
    jump Corridor


label Attic:
    scene bg attic with fade
    if visited_Attic == False:
        $ visited_Attic = True
        " - "
    
    "There is nothing left for you to do here, and you back to the corridor."
    scene bg black with fade 
    pause 0.5
    jump Corridor


label Bedroom:
    scene bg bedroom with fade
    " - "

    scene bg black with fade 
    pause 0.5
    jump Basement


label Basement:
    scene bg basement with fade
    " - "
    scene bg black with fade 
    pause 0.5
    jump Cave


label Cave:
    scene bg cave with fade
    " - "

    menu:
        "Creature":
            scene bg black with fade 
            pause 0.5
            jump End_Creature

        "Dark Ritual":
            scene bg black with fade 
            pause 0.5
            jump End_DarkRitual

        "Faint from headache":
            scene bg black with fade 
            pause 0.5
            jump End_Faint

label End_Creature:
    scene bg cave with fade
    " - "

    scene bg black with fade 
    pause 2.0
    return

label End_DarkRitual:
    scene bg cave with fade
    " - "
    
    scene bg black with fade 
    pause 2.0
    return

label End_Faint:
    scene bg cave with fade
    " - "
    
    scene bg black with fade 
    pause 2.0
    return

#label Entrance:
    # entrance scene


