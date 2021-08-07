from time import sleep


def about():
    text = """
    Hogwarts was founded over a thousand years ago by four powerful wizards: Godric Gryffindor, 
    Salazar Slytherin, Rowena Ravenclaw and Helga Hufflepuff. They chose to split the students 
    into four ‘houses’, each bearing their surnames and featuring young wizards and witches who 
    displayed abilities and personalities they wanted to nurture.

    To do this, Godric Gryffindor used his magical hat – henceforward known as the Sorting Hat 
    – to decide which children should go into which house, and so it has been ever since with a 
    yearly Sorting Ceremony that places each new pupil into their own new home.

    The four houses have different entry requirements, and nobody summed them up better than the 
    old Sorting Hat itself in its welcoming song...
    """
    for let in text:
        print(let, end="")
        sleep(0.008)
    sleep(5)


def start():
    print("""
            ░██████╗░█████╗░██████╗░████████╗██╗███╗░░██╗░██████╗░██╗░░██╗░█████╗░████████╗
            ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░██║░░██║██╔══██╗╚══██╔══╝
            ╚█████╗░██║░░██║██████╔╝░░░██║░░░██║██╔██╗██║██║░░██╗░███████║███████║░░░██║░░░
            ░╚═══██╗██║░░██║██╔══██╗░░░██║░░░██║██║╚████║██║░░╚██╗██╔══██║██╔══██║░░░██║░░░
            ██████╔╝╚█████╔╝██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░
            ╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

                                        [A] - Sorting
                                        [B] - Exit
        """)
