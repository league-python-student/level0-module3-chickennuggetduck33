import webbrowser
import time

bottle = 99
for i in range(97):
    print(str(bottle)+" bottles of beer on the wall "+str(bottle)+" bottles of beer")
    bottle = bottle - 1
    print("take one down pass it around "+str(bottle)+" bottles of beer on the wall")
print("2 bottles of beer on the wall 2 bottles of beer")
print("take one down pass it around 1 bottle of beer on the wall")
print("1 bottle of beer on the wall 1 bottle of beer")
print("take one down pass it around no more bottle of beer on the wall")
print("no more bottles of beer on the wall no more bottles of beer")
print("go to the store get some more 99 bottles of beer on the wall")
time.sleep(10)
webbrowser.open('https://i.pinimg.com/originals/21/a1/e6/21a1e6a2f7f5686ba23c23a1c7b47174.jpg')
