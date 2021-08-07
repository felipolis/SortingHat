## Sorting Hat

### About:

There are few things in the world that fit together. Harry Potter and Python are one of them.

I was wondering if I could make the Harry Potter universe sorting hat in python. However, how could I do this? If I set some random questions, how would I know which question would be the right one for a particular house?

It was then that I found in reddit a post from a user who got the analytics of the workings of the original Sorting Hat from the Pottermore site. I was intrigued because I needed to apply these analytics in a python algorithm to make my own Sorting Hat.

It is noteworthy that I used the same questions from the Pottermore quiz, as my intention was to recreate the original sorting hat, but in python.

Another important thing to say is that the test consists of 8 questions, however you will never answer the same questionnaire every time. There is a combination of several questions, as follows:

- First question: 3 possibilities

- Second question: 4 possibilities

- Third question: 5 possibilities

- Fourth question: 3 possibilities

- Fifth question: 3 possibilities

- Sixth question: 6 possibilities

- Seventh question: 1 possibility

- Eighth question: 3 possibilities

There are 3⋅1⋅3⋅3⋅4⋅5⋅6⋅3 = 9720 quiz combinations

It's not a lottery! The algorithm will analyze your answers and define which house you fit into. 

So, the goal is very simple: answer the questionnaire and find out which Hogwarts house you fit into.

### What did I use?

I've created something very simple with python, using pretty much just the standard library + pygame (to insert sounds).

- Python 3.9.2
- VirtualEnv 20.4.7
- All the other dependencies are already written in requirement.txt

### How to use?

- First of all, you need python3. [Click Here](https://www.python.org),
  download and install it.
- Secondly, you need to install all the packages i've used. On your project directory, open your command prompt and type:
  `pip install requirements.txt`
- Now you can run the program: `python SortingHat.py`


***Made by Felipe Archanjo.***
