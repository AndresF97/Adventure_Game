import time
import random
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
def intro():
    print_pause('Welcome to New Jersey, some people say that you can find the portal to hell \n')
    print_pause('luckly for you that your grandfather is a archyologist. \n')
    print_pause('You make your way into the New Jersey forrest were many trange creaters have been sighted! \n')
    print_pause('your father always told you to never go there, but your adventure spirit drives you to the unknown \n')
def Cave():
    print_pause('You\'ve entered the cave with the key that you stole from your father.')
    print_pause('You make your way into the ruins, you pull out the key')
    response = input('Would you like to put in the key "yes" or "no" \n')
    if 'yes' in response :
        print_pause('You have enetered the skull shape key in the hole\n' 'THE WALLS HAVE STARTED TO MOVE, all the bricks started to crumble\n')
        print_pause('the smell of sulfur starts to take over the room \n')
        Hell_Portal()
    else:
        print_pause('Your adventures spirit has died down, you put your head down in shame\n')
        print_pause('GAME OVER!')

        again = input ('would you like to play again "yes" or "no"\n')
        if 'yes' in again:
            intro()
            Cave()
            Hell_Portal()
        else:
            print_pause('Thank you for playing!')
def Hell_Portal():
    demons = random.choice(['little demon with small claws','Big demon with small t-rexc claws thats spits fire','fat demon that laughs like santa claus'])
    guns = random.choice (['1911 colt pistol','assult rifle','double-barrel shootgun'])
    power = random.choice(['in poor condition','in great condition','a broken condition'])
    print_pause(f'The portal opens, a {demons} comes out you grabe your trusty {guns} you check to see if its good condition')
    print_pause(f'Your gun is in {power}\n')
    gun_condition = power
    if 'poor' in gun_condition:
        print_pause('You use your gun. it is in poor condition''fourtunaley your gun worked, but it only shoot once. It wasnt very effective\n'
        'your gun broken......the demon approches you. He attacks you everything goes black.\n')
    elif 'great' in gun_condition:
        print_pause('You use your weapon... it was very effective. The Demon falls to its feet, you moved forward to you destiny')
        print_pause('You win!\n')
        again = input ('would you like to play again "yes" or "no"\n')
        if 'yes' in again:
            intro()
            Cave()
            Hell_Portal()
        else:
            print_pause('Thank you for playing!')
    elif 'broken' in gun_condition:
        print_pause('Your weapon has failed immidiatly, the demon has attacked you....EVERYTHING GOES DARK!!!!!\n')
        print_pause('GAME OVER \n')
        again = input ('would you like to play again "yes" or "no"\n')
        if 'yes' in again:
            intro()
            Cave()
            Hell_Portal()
        else:
            print_pause('Thank you for playing!')
def play_game():
    intro()
    Cave()

play_game()
