print('Welcome to your doom. Please select one of the options below:')
print('Cave')
print('Field')
print('Ocean')
print('Forest')

choice1 = input()
if choice1 == 'Cave':
    print('You have run into a troglodyte who bashes your brains in, finally releasing you from this mortal coil. Congratulations!')
    print('Game Over')
elif choice1 == 'Field':
    print('You find yourself in a tranquil field surrounded by cute bunnies and deer. The air is warm and you float on the tintillating aroma of wildflowers dancing in the breeze. You see a structure not too far in the distance. The sun is starting to set, but you believe you can make it there before nightfall. Do you go towards the structure?')
    choice2 = input()
    if choice2 == 'Yes':
        print('Placeholder')
    elif choice2 == 'No':
        print('The aroma of the field lures you into a deep slumber. When you awake, you realize that the warm embrace of the sun has gone and been replaced by the bitter chill of the night. You feel your entire body slowing down as the cold begins to take you.')
        print('Game Over')
    else:
        print('You fucked the code up and I do not know how to fix it. Thanks.')
elif choice1 == 'Ocean':
    print('A massive shark appears and starts swimming towards you. As you prepare for the inevitable attack, the water near you breaks and an even more massive shark appears and devours your would-be killer. He turns to you and says "There is always a bigger elasmobranch" before swallowing you whole.')
    print('Game Over')
elif choice1 == 'Forest':
    print('Idk, you find elves or some shit. You chose forest, of course it will be magical. You think you can survive a magical forest?')
    print('Game Over')
else:
    print('You fucked the code up and I do not know how to fix it. Thanks.')
