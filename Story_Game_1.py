#Story Game
#Created by Prateek Panwar, Story by Sanket Patil

#import playsound
import threading
from playsound.playsound import playsound
import time
#Import graphics
from graphics import graphics

#Variables
version = 1.7
global user_choice,question
question = 1
user_choice = 0
choice_value = [[[0] for i in range (1,3)] for i in range (1,10)]
questions_value = [[0] for i in range(1,10)]
picture = [[0] for i in range(1,14)]
name,birth_year = "",""
title = "Good or Bad or Ugly"
 
###Resources and declaration
#Show Picture of question
for i in range (1,14+1):
    picture.insert(i,graphics.graphics[i])

#questions_value
questions_value.insert(1,"""
You are walking on your way to home.In the air, you feel something unusual.
Everyone is watching you in a strange way.On the road, you saw a GOLDEN WATCH
with it's glass broken.
What will you do next?
""")
questions_value.insert(2,"""
Now you went home and saw that the watch is alrightand showing correct time.
Your mom saw the watch andtold you to give it to police as it may be stolen one.
What will you do next?
""")
questions_value.insert(3,"""
You gave the watch to a policeman and he died in just24 minutes.
Do you find yourself responsible??
""")
questions_value.insert(4,"""
The policeman you gave the watch died in 24 minutesand while dying, he didn't had
the watch. When youcasually checked your pocket, you got the watch which was showing
wrong time. You tried to reset the time andsuddenly a white light spread everywhere 
and you reachedanother place. You can see a grave written"""+name+"""on it.
You think that you have travelled time.
What will you do next?
""")
questions_value.insert(5,"""
So as a punishment, death has arrived (Press Y for yes and N for No)
Do you want to die?
What will you do next?
""")
questions_value.insert(6,"""
You tried to adjust time and go back, but you reached in an Almirah inside a house
and locked. You saw that a couple is fighting veryintensely. The wife is saying 
"It is the question of so many people's trust on me but, I will do if anyhow".
Husband replied "I will not make this possible. Now, it is my duty".And, they both
went out of home in two different directions. By thisconversation, you get to know
that you need to support the good and know what is going on. 
Whom will you follow?
""")
questions_value.insert(7,"""
You watched that the woman is trying to open the grave and steal something.
What will you do next?
""")
questions_value.insert(8,"""
Till this time, a feeling of love towards the wife has taken place inyour heart.
You follow the husband and he goes and makes a phone calland talks "At any cost,
I'm going to kill her" and you also saw a gunwith him.
What will you do next?
""")
questions_value.insert(9,"""
After killing her, you heared a voice "As punishment of killing yourwife
Death has arrived.
Do you want to die?
""")
questions_value.insert(10,"""
You killed him. Then you were taken to his grave, where it was written"""+name+"""-"""+birth_year+"""-2035
You saw his wife was tring to open the grave and steal something.
What will you do next?
""")
questions_value.insert(11,"""
You followed him to an old godown, where his wife was talking by whispering with someone.
When her husband reached there. She shocked and her husband pointed gun on her. 
Such position is there.
Do you want to die?
""")
questions_value.insert(12,"""
After killing her, you heared a voice "As punishment of killing your wife, death has arrived.
Do you want to die?
""")
questions_value.insert(13,"""
You killed him. Then you were taken to his grave, where it was written"""+name+"""-"""+birth_year+"""-2035
You saw his wife was tring to open the grave and steal something.
Do you want to die?
""")

#Question Choices
##question 1 choice 
choice_value[1].insert(1,"Pick up silently")
choice_value[2].insert(1,"Give to police since costly")
choice_value[3].insert(1,"Ignore and move on")
##question 2 choice
choice_value[1].insert(2,"Give it to police")
choice_value[2].insert(2,"Keep it secretly")
choice_value[3].insert(2,"Sell and get money")
##question 3 choice
choice_value[1].insert(3,"No")
choice_value[2].insert(3,"Yes")
choice_value[3].insert(3,"Police job is risky")
##question 4 choice
choice_value[1].insert(4,"Know what happened, without telling anyone")
choice_value[2].insert(4,"Try to go back by adjusting time")
choice_value[3].insert(4,"Observe quietly")
##question 5 choice
choice_value[1].insert(5,"Y - Yes")
choice_value[2].insert(5,"N - No")
choice_value[3].insert(5,"Y - Yes")
##question 6 choice
choice_value[1].insert(6,"Try to just save your life")
choice_value[2].insert(6,"Wife")
choice_value[3].insert(6,"Husband")
##question 7 choice
choice_value[1].insert(7,"Make partnership with her")
choice_value[2].insert(7,"Kill her and get what she wants")
choice_value[3].insert(7,"Warn her to not do so")
##question 8 choice
choice_value[1].insert(8,"Kill him just at that time")
choice_value[2].insert(8,"Explain him calmly and polietly")
choice_value[3].insert(8,"Follow him and find out more")
##question 9 choice
choice_value[1].insert(9,"Y - Yes")
choice_value[2].insert(9,"N - No")
choice_value[3].insert(9,"Y - Yes")
##question 10 choice
choice_value[1].insert(10,"Make partnership with her")
choice_value[2].insert(10,"Kill her and get what she wants")
choice_value[3].insert(10,"Warn her to not do so")
##question 11 choice
choice_value[1].insert(11,"Cut the rope and kill him")
choice_value[2].insert(11,"Let him kill her")
choice_value[3].insert(11,"Try to handle by peace")
##question 12 choice
choice_value[1].insert(12,"Y - Yes")
choice_value[2].insert(12,"N - No")
choice_value[3].insert(12,"Y - Yes")
##question 13 choice
choice_value[1].insert(13,"Make partnership with her")
choice_value[2].insert(13,"Help her")
choice_value[3].insert(13,"Stop her doing so")

###conclusions
def die(die_val):
    print("die!! fool!! "*1200,"\n\n")
    if (die_val == 1):
        print("You die!!! Fool, nothing is ignorable")
    if (die_val == 2):
        print("You die!!! Always listen to parents")
    if (die_val == 3):
        print("Whatever you think, You killed hime... Death has arrived")
    if (die_val == 4):
        print("Whatever you think, You killed hime... Death has arrived")
    if (die_val == 5):
        print("By sharing anything, you get peace of mind... die")
    if (die_val == 6):
        print("Selfishness gives death, you die!!!")
    if (die_val == 7):
        print("RIP! You die! She shot you by a gun")
    if (die_val == 8):
        print("She shot you by her gun, die.rip.")
    if (die_val == 10):
        print("Coward get lost. You must die!!!")
    if (die_val == 11):
        print("You got rest in peace, situation cannot be handled in peace. die")
def win():
    print("""
    Finally, You reached here...

    She: 'You helped me a lot. I feel a long relation from some other birth with you.
    So, let me clear my plan to you.
    
    "Some men came, caught you and took you some-where. You were thrown in a crowded place,
    then she pressed secret button in the ring of her husband which she had stollen from the
   grave and a bomb blasted". 

   By this, you first killed your future and your future wife killed you in future itself.'

    Death is inevietable, You are good, she was bad and ugly... you know""")
def half_blood_win():
    print(""" She: 'You helped me a lot. I feel a long relation from some other birth with you.
    So let me clear my plan to you. "Some men came, hold you she shot you" """)
def well_played():
    print("""
    So, as a punishment, death has arrived (Press Y or N to die)
    Do you want to die?  """)
    wp = input()
    if (wp == "y" or wp == "Y"):
        print(graphics.graphics[5])
        print("Here's your death wish, Rest in peace")
    if (wp == "n" or wp == "N"):
        print(graphics.graphics[5])
        print("Ah, I see you want to live. But death is inevitable. Rest in peace")

###Functions
#Choice Menu
def choice_menu(question):
   print("\n1.",choice_value[1][question],"\n2.",choice_value[2][question],"\n3.",choice_value[3][question])

#Each scene: single_que()
def single_que():
    global user_choice,question
    print(picture[question])
    print(questions_value[question])
    print(choice_menu(question))
    user_choice = int(input("Enter 1, 2 or 3 to choose your move: "))

#Main story
def main():
    global user_choice,question
##question 1 - junc
    question = 1
    single_que()
    #q1 c3
    if (user_choice == 3):
        die(1)
    #q1 c2
    if (user_choice == 2):
        question = 3
        single_que()
 #question 3
        #q3 c3
        if (user_choice == 3):
            die(4)
        #q3 c2
        if (user_choice == 2):
            die(3)
        #q3 c1
        if (user_choice == 1):
            question = 5
            single_que()
  #question 5
            well_played()

##question 1
    #q1 c1
    if (user_choice == 1):
        question = 2
        single_que()
 #question 2
    #q2 c3
        if (user_choice == 3):
            die(2)
    #q2 c2
        if (user_choice == 2):
            die(2)
    #q2 c1
        if (user_choice == 1):
            question = 4
            single_que()
  #question 4 - junc
            #q4 c1
            if (user_choice == 1):
                die(5)
            #q4 c3
            if (user_choice == 3):
                question = 7
                single_que()
     #question 7
                if (user_choice == 1):
                    die(8)
                if (user_choice == 3):
                    die(8)
                if (user_choice == 2):
                    question = 9
                    single_que()
                    well_played()
   #question 4
            #q4 c2
            question = 6
            single_que()
      #question 6
            #q6 c1
            if (user_choice == 1):
                die(6)
            #q6 c2
            if (user_choice == 2):
                die(7)
            #q6 c3
            if (user_choice == 3):
                question = 8
                single_que()
        #question 8
                #q8 c2
                if (user_choice == 2):
                    die(11)
                #q8 c1
                if (user_choice == 1):
                    question = 10
                    single_que()
          #question 10
                    #q10 c1
                    if (user_choice == 1):
                        die(8)
                    #q10 c3
                    if (user_choice == 3):
                        die(8)
                    #q10 c2
                    if (user_choice == 2):
                        question = 12
                        single_que()
            #question 12
                        well_played()
                #q8 c3
                if (user_choice == 3):
                    question = 11
                    single_que()
        #question 11
                    #q11 c3
                    if (user_choice == 3):
                        die(11)
                    #q11 c2
                    if (user_choice == 2):
                        die(10)
                    #q11 c1
                    if (user_choice == 1):
                        question = 13
                        single_que()
            #question 13
                        #q13 c1
                        if (user_choice == 1):
                            die(8)
                        #q13 c2
                        if (user_choice == 2):
                            win()
                        #q13 c3
                        if (user_choice == 3):
                            half_blood_win()

#Music playback
def playMusic():
    threading.Thread(target=playsound, args=("sound/a.mp3",), daemon=True).start()


#Main_Title
def title():
    print("Ver ",version)
    print("# Note: If you cannot watch frame below in one line, press Ctrl+Mouse scroll down to change windows font size\n")
    print("""+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+""")
    music = input("Enter a value: Music (off-0 / on-1): ")
    if (int(music) != 0):
        playMusic()
    print("\t"*3,title)
    name = input("\nEnter player's real name: ")
    birth_year = input("\nEnter Year of birth: ")
    print(picture[14])
    time.sleep(3) 
    main()
title()
