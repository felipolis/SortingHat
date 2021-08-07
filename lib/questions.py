from random import randint


def question(choices):
    while True:
        choice = str(input(">>>>> ")).strip().upper()[0]

        if choice in choices:
            return choice

        print("[WARNING] You should chose a defined option!!!")


def first_question():
    num = randint(1, 3)

    if num == 1:
        print("""
        Question 01: Dawn or dusk?

        [A] - Dawn
        [B] - Dusk
        """)
        choice = question("AB")
        if choice in 'A':
            return 1, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 1

    elif num == 2:
        print("""
        Question 01: Forest or river?

        [A] - Forest
        [B] - River
        """)
        choice = question("AB")
        if choice in 'A':
            return 1, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 1

    elif num == 3:
        print("""
        Question 01: Moon or stars?

        [A] - Moon
        [B] - Stars
        """)
        choice = question("AB")
        if choice in 'A':
            return 0, 1, 0, 1
        elif choice in 'B':
            return 1, 0, 1, 0


def second_question():
    num = randint(1, 4)

    if num == 1:
        print("""
        Question 02: Which of the following would you most hate people to call you?

        [A] - Ordinary
        [B] - Ignorant
        [C] - Cowardly
        [D] - Selfish
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 0, 1
        elif choice in 'B':
            return 0, 1, 0, 0
        elif choice in 'C':
            return 1, 0, 0, 0
        elif choice in 'D':
            return 0, 0, 1, 0

    elif num == 2:
        print("""
        Question 02: After you have died, what would you most like people to do when they hear your name?

        [A] - Miss you, but smile
        [B] - Ask for more stories about your adventures
        [C] - Think with admiration of your achievements
        [D] - I don't care what people think of me after I'm dead; it's what they think of me while I'm 
        alive that counts
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 0, 0, 0, 1

    elif num == 3:
        print("""
        Question 02: How would you like to be known to history?

        [A] - The Wise
        [B] - The Good
        [C] - The Great
        [D] - The Bold
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 0
        elif choice in 'C':
            return 0, 0, 0, 1
        elif choice in 'D':
            return 1, 0, 0, 0

    elif num == 4:
        print("""
        Question 02: Given the choice, would you rather invent a potion that would guarantee you:

        [A] - Love?
        [B] - Glory?
        [C] - Wisdom?
        [D] - Power?
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 0, 0, 0, 1


def third_question():
    num = randint(1, 5)

    if num == 1:
        print("""
        Question 03: Four boxes are placed before you. Which would you try and open?

        [A] - The small tortoiseshell box, embellished with gold, inside which some small creature 
        seems to be squeaking.
        [B] - The gleaming jet black box with a silver lock and key, marked with a mysterious rune 
        that you know to be the mark of Merlin.
        [C] - The ornate golden casket, standing on clawed feet, whose inscription warns that both 
        secret knowledge and unbearable temptation lie within.
        [D] - The small pewter box, unassuming and plain, with a scratched message upon it that 
        reads ‘I open only for the worthy.
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 0, 0, 0, 1
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 1, 0, 0, 0

    elif num == 2:
        print("""
        Question 03: Once every century, the Flutterby bush produces flowers that adapt their scent to 
        attract the unwary. If it lured you, it would smell of:

        [A] - A crackling log fire
        [B] - The sea
        [C] - Fresh parchment
        [D] - Home
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 1, 0, 0, 0
        elif choice in 'B':
            return 0, 0, 0, 1
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 0, 0, 1, 0

    elif num == 3:
        print("""
        Question 03: You enter an enchanted garden. What would you be most curious to examine first?

        [A] - The silver leafed tree bearing golden apples
        [B] - The fat red toadstools that appear to be talking to each other
        [C] - The bubbling pool, in the depths of which something luminous is swirling
        [D] - The statue of an old wizard with a strangely twinkling eye
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 0
        elif choice in 'C':
            return 0, 0, 0, 1
        elif choice in 'D':
            return 1, 0, 0, 0

    elif num == 4:
        print("""
        Question 03: Four goblets are placed before you. Which would you choose to drink?

        [A] - The foaming, frothing, silvery liquid that sparkles as though containing ground 
        diamonds.
        [B] - The smooth, thick, richly purple drink that gives off a delicious smell of chocolate 
        and plums.
        [C] - The golden liquid so bright that it hurts the eye, and which makes sunspots dance all 
        around the room.
        [D] - The mysterious black liquid that gleams like ink, and gives off fumes that make you see 
        strange visions.
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 0
        elif choice in 'C':
            return 1, 0, 0, 0
        elif choice in 'D':
            return 0, 0, 0, 1

    elif num == 5:
        print("""
        Question 03: What kind of instrument most pleases your ear?

        [A] - The violin
        [B] - The trumpet
        [C] - The piano
        [D] - The drum
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 0, 1
        elif choice in 'B':
            return 0, 0, 1, 0
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 1, 0, 0, 0


def fourth_question():
    num = randint(1, 3)

    if num == 1:
        print("""
        Question 04: Which of the following do you find most difficult to deal with?

        [A] - Hunger
        [B] - Cold
        [C] - Loneliness
        [D] - Boredom
        [E] - Being ignored
        """)
        choice = question("ABCDE")
        if choice in 'A':
            return 0, 1, 1, 0
        elif choice in 'B':
            return 0, 0, 1, 1
        elif choice in 'C':
            return 1, 0, 1, 0
        elif choice in 'D':
            return 1, 0, 0, 1
        elif choice in 'E':
            return 0, 1, 0, 1

    elif num == 2:
        print("""
        Question 04: A troll has gone berserk in the Headmaster’s study at Hogwarts. It is about 
        to smash, crush and tear several irreplaceable items and treasures. In which order would 
        you rescue these objects from the troll’s club, if you could?

        [A] - First, a nearly perfected cure for dragon pox. Then student records going back 1000 
        years. Finally, a mysterious handwritten book full of strange runes.
        [B] - First, student records going back 1000 years. Then a mysterious handwritten book full 
        of strange runes. Finally, a nearly perfected cure for dragon pox.
        [C] - First, a mysterious handwritten book full of strange runes. Then a nearly perfected 
        cure for dragon pox. Finally, student records going back 1000 years.
        [D] - First, a nearly perfected cure for dragon pox. Then a mysterious handwritten book full 
        of strange runes. Finally, student records going back 1000 years.
        [E] - First student records going back 1000 years. Then, a nearly perfected cure for dragon 
        pox. Finally, a mysterious handwritten book full of strange runes.
        [F] - First, a mysterious handwritten book full of strange runes. Then student records going 
        back 1000 years. Finally, a nearly perfected cure for dragon pox.
        """)
        choice = question("ABCDEF")
        if choice in 'A':
            return 1, 0, 1, 0
        elif choice in 'B':
            return 0, 0, 0, 1
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 1, 0, 0, 0
        elif choice in 'E':
            return 0, 0, 1, 1
        elif choice in 'F':
            return 0, 1, 0, 1

    elif num == 3:
        print("""
        Question 04: Which would you rather be:

        [A] - Envied?
        [B] - Imitated?
        [C] - Trusted?
        [D] - Praised?
        [E] - Liked?
        [F] - Feared?
        """)
        choice = question("ABCDEF")
        if choice in 'A':
            return 0, 1, 0, 1
        elif choice in 'B':
            return 0, 1, 0, 0
        elif choice in 'C':
            return 1, 0, 1, 0
        elif choice in 'D':
            return 1, 0, 0, 0
        elif choice in 'E':
            return 0, 0, 1, 0
        elif choice in 'F':
            return 0, 0, 0, 1


def fifth_question():
    num = randint(1, 3)

    if num == 1:
        print("""
        Question 05: If you could have any power, which would you choose?

        [A] - The power to read minds
        [B] - The power of invisibility
        [C] - The power of superhuman strength
        [D] - The power to speak to animals
        [E] - The power to change the past
        [F] - The power to change your appearance at will
        """)
        choice = question("ABCDEF")
        if choice in 'A':
            return 0, 1, 0, 1
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 0, 1, 1
        elif choice in 'D':
            return 0, 0, 1, 0
        elif choice in 'E':
            return 1, 0, 0, 1
        elif choice in 'F':
            return 0, 1, 0, 0

    elif num == 2:
        print("""
        Question 05: What are you most looking forward to learning at Hogwarts?

        [A] - Apparition and Disapparition (being able to materialize and dematerialize at will)
        [B] - Transfiguration (turning one object into another object)
        [C] - Flying on a broomstick
        [D] - Hexes and jinxes
        [E] - All about magical creatures, and how to befriend/care for them
        [F] - Secrets about the castle
        [G] - Every area of magic I can
        """)
        choice = question("ABCDEFG")
        if choice in 'A':
            return 1, 0, 0, 1
        elif choice in 'B':
            return 0, 1, 0, 0
        elif choice in 'C':
            return 1, 0, 1, 0
        elif choice in 'D':
            return 0, 0, 0, 1
        elif choice in 'E':
            return 0, 0, 1, 0
        elif choice in 'F':
            return 1, 0, 0, 0
        elif choice in 'G':
            return 0, 1, 0, 0

    elif num == 3:
        print("""
        Question 05: Which of the following would you most like to study?

        [A] - Centaurs
        [B] - Goblins
        [C] - Merpeople
        [D] - Ghosts
        [E] - Vampires
        [F] - Werewolves
        [G] - Trolls
        """)
        choice = question("ABCDEFG")
        if choice in 'A':
            return 1, 1, 0, 0
        elif choice in 'B':
            return 0, 1, 0, 0
        elif choice in 'C':
            return 0, 0, 1, 1
        elif choice in 'D':
            return 1, 1, 0, 0
        elif choice in 'E':
            return 0, 0, 0, 1
        elif choice in 'F':
            return 1, 0, 1, 0
        elif choice in 'G':
            return 0, 0, 1, 1


def sixth_question():
    num = randint(1, 6)

    if num == 1:
        print("""
        Question 06: You and two friends need to cross a bridge guarded by a river troll who insists 
        on fighting one of you before he will let all of you pass. Do you:

        [A] - Attempt to confuse the troll into letting all three of you pass without fighting?
        [B] - Suggest drawing lots to decide which of you will fight?
        [C] - Suggest that all three of you should fight (without telling the troll)?
        [D] - Volunteer to fight?
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 1, 0
        elif choice in 'C':
            return 0, 0, 0, 1
        elif choice in 'D':
            return 1, 0, 0, 0

    elif num == 2:
        print("""
        Question 06: One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling 
        Quill. Now he has come top of the class in Charms, beating you into second place. Professor 
        Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks 
        you whether or not your classmate used a forbidden quill. What do you do?

        [A] - Lie and say you don’t know (but hope that somebody else tells Professor Flitwick the 
        truth).
        [B] - Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your 
        classmate that if he doesn’t tell the truth, you will).
        [C] - Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he 
        deserves to be found out. Also, as you are both in the same house, any points he loses will be 
        regained by you, for coming first in his place.
        [D] - You would not wait to be asked to tell Professor Flitwick the truth. If you knew that 
        somebody was using a forbidden quill, you would tell the teacher before the exam started.
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 1, 0, 0
        elif choice in 'D':
            return 0, 0, 0, 1

    elif num == 3:
        print("""
        Question 06: A Muggle confronts you and says that they are sure you are a witch or wizard. Do you:

        [A] - Ask what makes them think so?
        [B] - Agree, and ask whether they’d like a free sample of a jinx?
        [C] - Agree, and walk away, leaving them to wonder whether you are bluffing?
        [D] - Tell them that you are worried about their mental health, and offer to call a doctor.
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 0, 0, 0, 1
        elif choice in 'C':
            return 1, 0, 0, 0
        elif choice in 'D':
            return 0, 0, 1, 0

    elif num == 4:
        print("""
        Question 06: Which nightmare would frighten you most?

        [A] - Standing on top of something very high and realizing suddenly that there are no hand- 
        or footholds, nor any barrier to stop you falling.
        [B] - An eye at the keyhole of the dark, windowless room in which you are locked.
        [C] - Waking up to find that neither your friends nor your family have any idea who you are.
        [D] - Being forced to speak in such a silly voice that hardly anyone can understand you, and 
        everyone laughs at you.
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 1, 0, 0
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 0, 1, 0
        elif choice in 'D':
            return 0, 0, 0, 1

    elif num == 5:
        print("""
        Question 06: Which road tempts you most?

        [A] - The wide, sunny, grassy lane
        [B] - The narrow, dark, lantern-lit alley
        [C] - The twisting, leaf-strewn path through woods
        [D] - The cobbled street lined with ancient buildings
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 0, 0, 0, 1
        elif choice in 'C':
            return 1, 0, 0, 0
        elif choice in 'D':
            return 0, 1, 0, 0

    elif num == 6:
        print("""
        Question 06: Late at night, walking alone down the street, you hear a peculiar cry that you 
        believe to have a magical source. Do you:

        [A] - Proceed with caution, keeping one hand on your concealed wand and an eye out for any 
        disturbance?
        [B] - Draw your wand and try to discover the source of the noise?
        [C] - Draw your wand and stand your ground?
        [D] - Withdraw into the shadows to await developments, while mentally reviewing the most 
        appropriate defensive and offensive spells, should trouble occur?
        """)
        choice = question("ABCD")
        if choice in 'A':
            return 0, 0, 1, 0
        elif choice in 'B':
            return 1, 0, 0, 0
        elif choice in 'C':
            return 0, 0, 0, 1
        elif choice in 'D':
            return 0, 1, 0, 0


def seventh_question():
    print("""
    Question 07: If you were attending Hogwarts, which pet would you choose to take with you?

    [A] - Tabby cat             [F] - Tawny owl             [K] - Common toad
    [B] - Siamese cat           [G] - Screech owl           [L] - Natterjack toad
    [C] - Ginger cat            [H] - Brown owl             [M] - Dragon toad
    [D] - Black cat             [I] - Snowy owl             [N] - Harlequin toad
    [E] - White cat             [J] - Barn owl              [O] - Three toed tree toad
    """)
    choice = question("ABCDEFGHIJKLMNO")
    if choice in 'A':
        return 1, 0, 0, 1
    elif choice in 'B':
        return 0, 0, 0, 1
    elif choice in 'C':
        return 0, 0, 0, 1
    elif choice in 'D':
        return 0, 0, 0, 1
    elif choice in 'E':
        return 0, 0, 0, 1
    elif choice in 'F':
        return 0, 1, 0, 0
    elif choice in 'G':
        return 0, 1, 0, 0
    elif choice in 'H':
        return 0, 1, 0, 0
    elif choice in 'I':
        return 0, 1, 1, 0
    elif choice in 'J':
        return 0, 1, 0, 0
    elif choice in 'K':
        return 0, 0, 1, 0
    elif choice in 'L':
        return 0, 0, 1, 0
    elif choice in 'M':
        return 1, 0, 1, 0
    elif choice in 'N':
        return 0, 0, 1, 0
    elif choice in 'O':
        return 0, 1, 1, 0


def eighth_question():
    num = randint(1, 3)

    if num == 1:
        print("""
        Question 08: Black or White

        [A] - Black
        [B] - White
        """)
        choice = question("AB")
        if choice in 'A':
            return 1, 0, 0, 1
        elif choice in 'B':
            return 0, 1, 1, 0

    if num == 2:
        print("""
        Question 08: Heads or Tails

        [A] - Heads
        [B] - Tails
        """)
        choice = question("AB")
        if choice in 'A':
            return 0, 1, 1, 0
        elif choice in 'B':
            return 1, 0, 0, 1

    if num == 3:
        print("""
        Question 08: Left or Right

        [A] - Left
        [B] - Right
        """)
        choice = question("AB")
        if choice in 'A':
            return 0, 1, 0, 1
        elif choice in 'B':
            return 1, 0, 1, 0
