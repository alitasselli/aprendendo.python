import serial
buttonState = serial.Serial('/dev/cu.usbmodem1421', 9600)
#estado inicial do button
buttonStatebeforepress = int(0)
#condicao de execucao.
buttonpress = b'0'
isRunning = True
while isRunning:
    buttonpress = int(buttonState.readline().strip())
   # print(int(buttonpress))
   # print(int(buttonStatebeforepress))

    if buttonStatebeforepress != buttonpress:
        print("mudou estado do butão")
        #isRunning = False
       # print("saindo do programa")
       ## buttonStatebeforepress = buttonpress
