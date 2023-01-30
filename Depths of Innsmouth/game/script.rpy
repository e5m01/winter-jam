# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Naming convenction:   
#   c_ for Charater 
#   b_ for Backgrounds
#   m_ for Music Tracks


# Choice Flags
default Sword_taken = False
default Ttka_Halot_taken = False
default Clue_taken = False

default visited_Corridor = False
default visited_Library = False
default visited_Attic = False
default visited_Bedroom = False

define diss = Dissolve(0.5)


# Game starts here.
label start:
    
    #jump RunCredits
    stop music fadeout 2
    pause 2.0

    #############
    # INTRO SCENE
    scene bg-black
    play music "Audio - creepy leaves at night.wav" fadeout 5 fadein 10
    pause 1.0
    #play music "Depth of Innsmounth.mp3"
    
    "You don't exactly know how you got here. There's a void in your head."
    "But you can still remember who you are, and what you're doing here."
    "You are a game developer at a very prominent game studio, and you used your savings to take a trip with your friends to England, where you live."
    "You are all fans of horror stories and board games, and there are a couple of Narrative Designers in the group..."
    "... who, when they saw Innsmouth's name on the map, got curious."
    "They let you know that Innsmouth is the fictional name of an American town in one of Lovecraft's stories."
    "You were passing through anyway and the sun was setting. So you decided that spending a night in Innsmouth would be thrilling."
    "But the rest, as soon as you crossed the border of that eerie little town ... is hazy, in your memories."
    
    scene bg-mansion with fade

    "You gaze at the unsettling manor house looming before you. Thin spires reaching obliquely toward the sky, with tiles blackened as if burnt out by a fire."
    "Even the gray stone of which the castle's exterior is made, it reminds one of an insane pallor, close to death."
    "All around the manor, the diseased and leafless trees seem to bend in your direction, with irregular and sinister articulations of the branches, in what seems to be an expression of grief."
    "You look around, and you realize-that you are engulfed in darkness. You see nothing behind you-but you hear the creaking of wood, the confused rustling of leaves, and more sounds you can't quite understand."
    "A chill runs through your body. Where are the others? What has happened to them? There is no sign of them, and you begin to think that you should find shelter from the darkness."
    "So you make your way to the entrance of the manor house."

    scene bg-black with fade 

    play sound "Audio - door handle.wav"
    pause 1.25

    jump EntranceHall

label EntranceHall:
    stop music fadeout 2
    play sound "Audio - big door opening.wav"
    pause 5.25
    play music "Depth of Innsmounth.mp3" fadein 10

    scene bg-corridor with fade
    
    "Nonostante le luci accese, la tua prima impressione è che questo luogo sia stato abbandonato a sé stesso."
    "L'aria di questo luogo sembra più rarefatta- come una nebbia altamente improbabile. Potrebbe essere polvere, o cenere."
    "Ti trovi in quello che sembrerebbe essere una grande entrance hall, con delle scale che portano verso l'alto."
    "Una delle stanze al piano di sopra sembra aperta, forse uno studio di qualche genere."
    "L'altra parte della scala, invece, porta direttamente all'attico."
    "Questo piano sembra portare a un lungo corridoio, difficile sapere dove potrebbe farti finire."

    menu:
        "Library":
            scene bg-black with fade 
            pause 2.0
            jump Library

        "Attic":
            scene bg-black with fade 
            pause 2.0
            jump Attic

        "Corridor":
            scene bg-black with fade 
            pause 2.0
            jump Corridor


label Library:
    scene bg-library with fade
    $ visited_Library = True

    "You stand in a dusty studio. The smell of old paper and ink fills your nostrils."
    "In front of you stands a desk of fine wood, with wavy legs and a surface covered with a glass plate in which elegant decorations are carved."
    "It is impossible to decipher the decorations, for the table is almost entirely taken up by tomes haphazardly stacked on top of each other, yellowed papers, fountain pens and ink nibs."
    "The walls of the room are mostly taken up by ceiling-high bookcases with countless books and knick-knacks."
    "You look around, and your attention is caught by an artifact that, of all things, seems strange to find in a study."
    
    if Sword_taken is False:
        play sound "Audio - blade stroking.wav"
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

    if Ttka_Halot_taken is False:
        "You walk back to the door, and in doing so you hear a thud. You accidentally dropped a book."
        "When you pick it up to put it back, you notice that it is a smoke-gray tome with a leather cover where symbols are inscribed."
        "They look like occult symbols going around a circle, and at the bottom is the title:"
        "T'tka Halot."

        play sound "Audio - pages shuffling.wav" fadein 5
        pause 3

        "You open it. The book contains a series of hand-made illustrations, so old that the ink, formerly black, has changed color along with the yellowing of the pages."
        "You don't understand anything written in it, but they look like some sort of chants."

        stop sound fadeout 2
        "Do you want to take the T'tka Halot?"
        
        menu:
            "Yes":
                $ Ttka_Halot_taken = True
                play sound "Audio - item taken.wav"

            "No":
                $ Ttka_Halot_taken = False

    
    "Where do you want to go next?"
    menu:
        "Attic":
            scene bg-black with fade
            pause 3.0
            jump Attic

        "Corridor":
            scene bg-black with fade
            pause 3.0
            jump Corridor


label Attic:
    scene bg-attic with fade
    
    if visited_Attic is False:
        $ visited_Attic = True
        "As you climb the stairs leading to the attic, you realize that the lights do not reach the upper floor."
        "You try to help yourself with the flashlight on your smartphone."

        play sound "Audio - stairs creaking.wav" fadein 2
        pause 2.0

        "The stairs creak under your feet, lit by the sharp, bright light of the flashlight."
        "They lead you to a short landing, and before you stands a door."
        "You try to open it. The brass handle squeaks as it goes along with you."

        stop sound fadeout 2

        play sound "Audio - door handle.wav" fadeout 2
        pause 2.0

    " In front of you there is a dusty room, filled with junk that, in the cold light, seems to twist and extend into distorted shapes, merging with its own shadow..."
    "... to the point that you are no longer sure where the silhouette of a wrapped Persian rug ends..."
    "... and where the corner of an old curtain, set by the window, begins."
    "There is no sign of your friends here. Nor of anything useful. But maybe you can find some information about what this manor is..."
    "You look around. Old photographs, moldy books, mirrors covered with yellowed drapes."
    stop sound fadeout 2

    if Clue_taken is False:
        "A fabric box, among other things, seems to contain a set of documents."
        "Do you want to take a look?"
        menu:
            "Yes":
                $ Clue_taken = True
                play sound "Audio - item taken.wav"
                jump Attic__clue

            "No":
                $ Clue_taken = True
                jump Attic__no_clue
    else: 
        jump Attic__clue

label Attic__clue:
    "You crouch down to search for anything interesting between folders, construction maps, and old paper."
    "Your hand picks out an old picture. It portrays a man, a woman and two children, posing behind the mansion."
    "The mansion looks very similar to the one you are in now. The man and woman are smiling, they look happy."
    "There's something about their looks that doesn't sit right with you, though. Theirs is a glazed look, and around their necks they wear pendants."
    "You bring the flashlight closer to the picture to try to get a better look. Those pendants seem to have the shape of a sea animal, like an octopus, or a squid."
    "They are wearing fine clothes, the kind that was in fashion no longer than 70 years ago."
    "You bring your gaze to the fabric box again, and one of the mansion's maps catches your eye. You reach out your hand, and bring it in front of the flashlight."

    play sound "Audio - pages shuffling.wav" fadein 5
    pause 2.0

    "The map seems to accurately depict the floors of the manor. The attic, where you are standing, is the highest floor."
    "Below that is the study, a bathroom, and a couple of other rooms whose function you can't quite understand."
    "After that, the hallway seems to lead to the kitchens, and the bedrooms."
    "You wrinkle your forehead when you notice that the floors, in fact, are not finished."
    "There seems to be a basement. But what's more strange is that the access door to the basement seems to be located..."
    "... in one of the bedrooms, through a trap door."
    "You don't know why, but you start to feel the hair on your arms rise, and a shiver starts from the back of your neck, as if your survival instincts had noticed something you hadn't."
    "You sigh, and you're about to put everything back in place, when you spot a symbol next to the hatch drawing."
    "It's the same symbol you saw around the necks of the two landlords."
    "That detail sticks in your mind as you abandon the papers in the box, standing up."
    stop sound fadeout 2
    pause 0.5
    
    jump Attic__no_clue

label Attic__no_clue:

    "Where do you want to go now?"
    menu:
        "Library":
            jump Library

        "Corridor":
            jump Corridor


label Corridor:
    scene bg-corridor with fade
    $ visited_Corridor = True

    "You walk down the hallway to the ground floor. You proceed down the corridor, and you seem to hear, from inside the manor, still the rustling of the branches outside."
    "Perhaps it is the sound of the floorboards under your weight. Or the wooden furniture, due to the dampness. Maybe there's someone...? Your friends...?"
    "You get a little dizzy, and as you go on, turning on the flashlight of your phone to see clearly, you begin to feel a strong headache gripping you."
    "You stop when you notice a light coming from one of the rooms. The door is open."
    "You walk in, observe the room. The bed is diagonal, like it had been moved. On the floor, where the bed was supposed to be, seems to be a trapdoor."
    "The trapdoor was fastened to the floor by a chain clamped around two metal circles fused with the wooden boards. That chain is now unraveled."
    "Something inside you is drawn by the curiosity of seeing what's underneath. The other part of you, on the other hand, has the impression that the corners of the walls are shrinking against themselves, that the room is being sucked in by that same trapdoor."
    "The headache gets worse."

    "It's your choice, but something tells you that if you go down the trapdoor now, you won't be able to come back."

    menu:
        "Go down":
            jump Cave

        "Don't go down":
            menu:
                "Attic":
                    jump Attic

                "Library":
                    jump Library


label Cave:
    scene bg-cave with fade
    
    "You crouch toward the trapdoor, grab the chain and lift it to open the hole."
    "With an ominous creak, the wooden square lifts up on its pivot, revealing steep stairs that sink into the darkness."
    "You dip your legs into that void, and thanks to the flash of your smartphone you can see where your feet rest."
    "You grab the metal handrail to help you down the stairs, and at one point the soles of your shoes meet the concrete."
    "An almost completely empty basement is what the light from your smartphone reveals. And at the bottom of the basement, another door."
    "The headache is becoming almost unbearable, and your body shivers from the cold."
    "There must be something down there, but you can't tell why you think so."
    "You move forward, and after the door you see more stairs, more downhill, this time dug directly into the stone, into ancient damp, mold-covered furrows."
    "You descend in a time that seems infinite, and you have the feeling that the deeper you go into that sort of cave, the more the laws of time and space are dilating."
    "The stairs end. A series of tunnels open before you, dimly lit by a few lanterns."
    "You can hear, at the bottom, voices reciting chants. Your head begins to spin. Somehow, you still manage to keep your balance."
    "You head in the direction of the chants, and the scene that unfolds before you is chilling."
    "People wrapped in hoods stand in a circle before a symbol inscribed on the floor. They have tomes in their hands, from which they read the verses they are reciting."
    "But the thing that makes you shudder is that from that symbol inscribed on the floor there seems to emerge a sinister aura, which, somehow, your body manages to perceive as deeply dangerous and evil."
    
    play music "Depth of Innsmounth.mp3" fadein 2.0
    
    "And if your gaze doesn't betray you yet, right there in the perimeter of the symbol, tentacles begin to emerge -- from the floor."
    "Quick, try to figure out what you should do."

    if Sword_taken is True:
        "You carry that sword you found in the study. You can hit those cultists and stop the ritual."
    
    if Ttka_Halot_taken is True:
        "You carry the book called 'T'tka Halot.' You can use it to join the ritual as well and side with the cultists in creating a new world."
        "Or you can use it to break the ritual and reverse the spell, sucking the cultists inside the summoning symbol."

    # trigger end
    if Sword_taken is True and Ttka_Halot_taken is False:
        jump End_Sword
    if Sword_taken is False and Ttka_Halot_taken is True:
        jump End_Book
    if Sword_taken is True and Ttka_Halot_taken is True:
        jump End_SwordAndBook

label End_Sword:
    "Do you want to use the sword?"
    menu:
        "Yes":
            jump End_Sword_uses

        "No":
            jump BadEnding

label End_Sword_uses:
    
    "Quickly, you draw your sword. You're not sure how to use it, but you imagine you can just twirl it in the air and strike someone with it to end the ritual."
    "That's what you do. You throw yourself at one of the cultists and hit him with the sword."

    play sound "Audio - blade stroking.wav"
    pause 2.0
    
    "You manage to hit one of them, breaking the chorus. An ominous beam of red light radiates from the portal, and you hear a distant screeching coming from there, what sounds like it belongs to a creature you've never heard before."
    "The tentacles retreat, and slowly that beam of light thins until it disappears."
    "You managed to prevent the ritual, but soon the joy of having saved humanity is replaced by a sharp feeling in your lungs."
    "One of the cultists stabbed you in the back. You feel your legs weak, and you fall to your knees."
    "You lie down, feeling your head spin. Soon you lose consciousness, but at least you do so with the knowledge that humanity is safe, at least this time, thanks to you."

    jump RunCredits

label End_Book:
    "What do you want to use the book for?"
    menu:
        "I don't want to do anything":
            jump BadEnding

        "I want to break the ritual":
            jump End_Book_good

        "I want to join the cultists":
            jump End_Book_bad

label End_Book_good:
    " You pull out the book, and quickly look for a spell that can break the ritual."
    "You find it. You start reciting the verses written on the tome."
    "An ominous beam of red light radiates from the portal, and you hear a distant screeching coming from there, what sounds like it belongs to a creature you've never heard before."
    "The cultists turn to look at you, and try to stop you, drawing their daggers. But before they can reach you, they start getting sucked into the same portal they've opened."
    "Amid the screams of the cultists, the tentacles of the monstrous creature retreat, and slowly that ray of light thins until it disappears."
    "You managed to prevent the ritual. You, your friends, and all humanity are saved."
    "Happy, you walk along the trail of the cavern until you emerge from it. The cavern flows out into the sea, giving you a view of the dark depths beneath your feet."
    
    scene bg-black with fade
    "For now humanity is safe, and you hope it will remain so for a long time to come."
    
    jump RunCredits

label End_Book_bad:
    "You want to be part of the story, yes. The story of how humanity was ended."
    "Hard to know who will ever tell that story, maybe Azatoth themselves."
    "But that's what you want. And so, you pull out the book, flip through it, try to recognize those verses that the cultists are reciting."
    "And when you find them, you stand beside them and also chant to bring Cthulhu into this plane."
    "With your help, the cultists' chanting becomes more and more powerful. Soon the ominous portal widens to give more and more space to that creature that spreads its tentacles along the floor."
    "The tentacles pile up, until there is enough space for a monstrous, gigantic, sea-like creature to emerge."
    "The creature, right before your eyes, emits an unnatural screech that makes you shudder with an odd exaltation."
    "You begin to hear, in the distance, the sound of the sea churning, and of thunder heralding bad weather."
    "The cultists recite a hymn, kneel to the monstrous creature, and you do the same."
    "It drags itself toward the sea, and you raise your face to admire it."

    scene bg-black with fade
    "Soon you will witness the end of all that you know. And you look forward to it."
    
    jump RunCredits


label End_SwordAndBook:
    "What tool do you want to use?"
    menu:
        "Sword":
            jump End_Sword_uses

        "Book":
            jump End_Book

        "Nothing":
            jump BadEnding

label BadEnding:
    "Helpless, you watch the cultists perform the ritual before your eyes."
    "The portal slowly unravels from the cavern floor, widening, and a red light colors the stone walls."
    "The tentacles build up, until there is enough space for a monstrous, gigantic, sea-like creature to emerge."
    "The creature does not notice you, but surrounded by the cultists it emits an unnatural screech that makes your skin crawl."
    "You begin to hear, in the distance, the sound of the sea churning, and thunder heralding bad weather."
    "The cultists recite a hymn, kneel to the monstrous creature, and as it drags itself toward the sea, your headache prevents you from reacting."
    "You fall to your knees, in a whimper."

    scene bg-black with fade
    "Slowly, you lose consciousness, and deep inside you know, that it's over. Not only for you, but for all of us."

    jump RunCredits


label RunCredits:
    scene bg-black with fade

    show text "{size=70}The End{/font}":
    with diss

    play music "Audio - creepy leaves at night.wav" fadeout 2 fadein 10
    pause 5.0
    hide text
    with diss
    pause 0.5

    #centered "{size=+75}{cps=8}Written By:\n\nThewellreadredhead{/cps}{/size}{p=5.0}{nw}"
    show text "{size=60}{color=#3b5758}Credits{/font}{/color}" as textCredits:
        xalign 0.5
        yalign 0.3
    with diss
    pause 2.0
    hide text
    with diss
    pause 0.5

    show text "{size=38}{color=#97bfbe}Written by {b}Erica Bellucci{/b}{/font}{/color}" as text1:
        xalign 0.5
        yalign 0.425
    with diss
    pause 2.0
    
    show text "{size=38}{color=#97bfbe}Scripted by {b}Anja Schiffner{/b}{/font}{/color}" as text2:
        xalign 0.5
        yalign 0.5
    with diss
    pause 2.0
    
    show text "{size=38}{color=#97bfbe}Music & Sound Design by {b}David Requena{/b}{/font}{/color}" as text3:
        xalign 0.5
        yalign 0.575
    with diss
    pause 2.0
    
    show text "{size=38}{color=#97bfbe}Images from {b}www.pixabay.com{/b}{/font}{/color}" as text4:
        xalign 0.5
        yalign 0.675
    with diss
    pause 2.0

    hide textCredits
    hide text1
    hide text2
    hide text3
    hide text4
    with diss
    pause 2.0
    
    stop music fadeout 5.5
    show text "{size=38}Thank you for playing ♥{/font}":
    with diss
    pause 5.0
    hide text
    with diss
    pause 0.5
    
    return

#################################################################################
### Test Jumps
### these are only used to test audio, music or UI 

label TEST_Audio:
    "Audio - big door opening"
    play sound "Audio - big door opening.wav"
    pause 5.0
    "Audio - blade stroking"
    play sound "Audio - blade stroking.wav"
    pause 7.0
    "Audio - book dropped"
    play sound "Audio - book dropped.wav"
    pause 2.0
    "Audio - door handle"
    play sound "Audio - door handle.wav"
    pause 2.0
    "Audio - item taken"
    play sound "Audio - item taken.wav"
    pause 2.0
    "Audio - stairs creaking.wav"
    play sound "Audio - stairs creaking.wav"
    pause 6.0
    "Audio - woodboards creaking.wav"
    play sound "Audio - woodboards creaking.wav"
    pause 6.0
    "Audio - pages shuffling.wav"
    play sound "Audio - pages shuffling.wav"
    pause 20.0
    "Audio - creepy leaves at night.wav"
    play sound "Audio - creepy leaves at night.wav"
    pause 20.0

label TEST_Music:
    "Depth of Innsmounth.mp3"
    play music "Depth of Innsmounth.mp3"
    pause 5.0

    "Depth of Innsmounth - Intense.mp3"
    play music "Depth of Innsmounth - Intense.mp3"
    pause 5.0

label TEST_UI_dialogue:
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

label TEST_UI_options:
    "UI test"
    menu:
        "Creature":
            pause 1.0

        "Dark Ritual":
            pause 1.0

        "Faint from headache":
            pause 1.0
    "UI test end"