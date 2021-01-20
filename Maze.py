maze_list= []
leaderboardtemplist = []

function_list = ['Read and load maze from file','View maze','Play maze game','Configure current maze','Export maze to file','Create new maze','Play maze using SenseHAT','View Leaderboard']
configuration_list = ['Create wall','Create passageway','Create start point','Create end point','Main Menu']
leaderboardprint_list = []

#==============================================================================================================
#==============================================================================================================

#Show menu list
def mazemenu():
    for i in range(len(function_list)):
            print('[{}] {}' .format(i+1, function_list[i]))
    print('\n[0] Exit Maze')
        
#Open .csv file
def openmaze(filename):
        maze_list.clear() #clear current list
        try:
                file = open(filename,'r')
                for line in file:
                        line = line.strip('\n')
                        maze_list.append(list(line))
        except IOError:
                print('Error, File name/type does not exist')
        return maze_list

#View the maze
def viewmaze(filename):
        for i in range(len(maze_list)):
                print(maze_list[i]) #print maze in a orderly manner

#============================================================================================================
#==============================================================================================================

#print the location of A/B
def mazeviewlocation(aorb):
        for row in range(len(maze_list)):
                                for col in range(len(maze_list[row])):
                                        if maze_list[row][col]==aorb:
                                                print('Location of End ({}) - (Row{}, Column{})'.format(aorb,row+1,col+1))

#Play the maze
def playmaze(movenumber,movenumber2):
        userinput = False
        for row in range(len(maze_list)):
                for col in range(len(maze_list[row])):
                        if maze_list[row][col]=='A':
                                if maze_list[row+int(movenumber)][col+int(movenumber2)] == 'O':
                                        maze_list[row+int(movenumber)][col+int(movenumber2)] = 'A'
                                        maze_list[row][col] = 'O'
                                        viewmaze(filename)
                                        mazeviewlocation('A')
                                        mazeviewlocation('B')
                                        userinput = True
                                elif maze_list[row+int(movenumber)][col+int(movenumber2)] == 'B':
                                        maze_list[row+int(movenumber)][col+int(movenumber2)] = 'A'
                                        maze_list[row][col] = 'O'
                                        userinput = True
                                elif maze_list[row+int(movenumber)][col+int(movenumber2)] == 'X':
                                        print('Invalid movement, please try again.')
                                        userinput = True
                                elif maze_list[row+int(movenumber)][col+int(movenumber2)] == '':
                                        print('Invalid movement, please try again.')
                                        userinput = True
                                else:
                                        continue
                        if userinput == True:
                                break

#To record A or B position in the maze
def ABrecord(varAorB,stringofAorB):
        for row in range(len(maze_list)):
                for col in range(len(maze_list[row])):
                        if maze_list[row][col]== varAorB:
                                stringofAorB = [row,col] # if the row and col == A/B (depending in the call function), record the row and col of it
        return stringofAorB

#To restart maze
def restartplaymaze():
        for row in range(len(maze_list)):
                for col in range(len(maze_list[row])):
                        if maze_list[row][col]=='A':
                                maze_list[row][col] = 'O' #replace current A to O
        
        maze_list[int(mazeApos[0])][int(mazeApos[1])] = 'A' #use the recorded location of A and replace it back
        maze_list[int(mazeBpos[0])][int(mazeBpos[1])] = 'B' #use the recorded location of B and replace it back

#==========================================================================================================
#==============================================================================================================

#Show configuration menu list
def configmenu():
        print('\nCONFIGURATION MENU\n=================')
        for i in range(len(configuration_list)):
            print('[{}] {}' .format(i+1, configuration_list[i]))
        
#Configuration option and if user choose to configure, split the number into a list and change the letter according to the call function stated
def configcut(letter):
        print('=========================================')
        viewmaze(filename)
        print('Enter the coordinate of the line you wish to change E.g. Row,Column')
        print('\'B\' to return to Configure Menu.')
        Bfound = False
        Mfound = False
        configchoice = input('\'M\' to return to Main Menu: ')
        if configchoice == 'B':
                Bfound = True
        elif configchoice == 'M':
                Mfound = True
        else:
                try:
                        confposition = configchoice.split(',')
                        maze_list[int(confposition[0])-1][int(confposition[1])-1] = letter
                        viewmaze(filename)
                except ValueError:
                        print('Invalid Input, please enter again.')
        return [Bfound,Mfound] #return the list whether to return to config menu or go back to main menu or none

#==============================================================================================================
#==============================================================================================================

#play the maze using sensehat
def playmazepi(movenumber,movenumber2):
    userinput = False
    for row in range(len(maze_listpi)):
        for col in range(len(maze_listpi[row])):
            if maze_listpi[row][col]==A:
                if maze_listpi[row+int(movenumber)][col+int(movenumber2)] == O:
                    maze_listpi[row+int(movenumber)][col+int(movenumber2)] = A
                    maze_listpi[row][col] = O
                    userinput = True
                elif maze_listpi[row+int(movenumber)][col+int(movenumber2)] == B:
                    maze_listpi[row+int(movenumber)][col+int(movenumber2)] = A
                    maze_listpi[row][col] = O
                    userinput = True
                elif maze_listpi[row+int(movenumber)][col+int(movenumber2)] == X:
                    print('Invalid movement, please try again.')
                elif maze_listpi[row+int(movenumber)][col+int(movenumber2)] == '':
                    print('Invalid movement, please try again.')
                else:
                    continue
            if userinput == True:
                break

#restart the maze in sensehat
def restartplaymazepi():
    for row in range(len(maze_listpi)):
        for col in range(len(maze_listpi[row])):
            if maze_listpi[row][col]==A:
                maze_listpi[row][col] = O
        
    maze_listpi[int(mazeApospi[0])][int(mazeApospi[1])] = A
    maze_listpi[int(mazeBpospi[0])][int(mazeBpospi[1])] = B

#view the location in the raspberry pi's python console
def mazeviewlocationpi(aorb):
    for row in range(len(maze_listpi)):
        for col in range(len(maze_listpi[row])):
            if maze_listpi[row][col]==aorb:
                print('Location of End ({}) - (Row{}, Column{})'.format(aorb,row+1,col+1))
#==============================================================================================================
#==============================================================================================================

print('MAIN MENU\n=========')
mazemenu()
#User's option in main menu
while True:
        try:
                select = int(input('Enter your option: '))
        except ValueError:
                print('Invalid Input, please try again')
                continue
        
        #open file and save under maze_list
        if select == 1:
                maze_list = []
                print('Option [{}] Read and load maze from file\n'.format(select))
                filename = input('Enter the name of the data file: ')
                openmaze(filename)
                line_read = int(len(maze_list))
                line_read += 1
                print('Number of line read: {}\n'.format(line_read))
                mazemenu()
#==============================================================================================================
#==============================================================================================================
        #view maze
        elif select == 2:
                viewmaze(filename)
#==============================================================================================================
#==============================================================================================================
        #play maze
        elif select == 3:
                #Print the maze and the option chosen
                print('Option [{}] Play maze game\n\n========================================='.format(select))
                viewmaze(filename)

                #Locate the row and col of A and B
                for row in range(len(maze_list)):
                                for col in range(len(maze_list[row])):
                                        if maze_list[row][col]== 'A':
                                                mazeApos = [row,col]

                for row in range(len(maze_list)):
                                for col in range(len(maze_list[row])):
                                        if maze_list[row][col]== 'B':
                                                mazeBpos = [row,col]
                #Shows the Coordinate of A
                mazeviewlocation('A')

                #Shows the Coordinate of B
                mazeviewlocation('B')

                #leaderboard points
                leaderboardscore = 10000

                #Playing the maze codes
                endmaze = False
                while True:
                        if maze_list[int(mazeBpos[0])][int(mazeBpos[1])] == 'A':
                                #Leaderboard codes
                                playername = input('Your score is {}, please enter you name: '.format(leaderboardscore))
                                leaderboardtemplist = [playername,leaderboardscore]
                                leaderboardprint_list.append(leaderboardtemplist)
                                print('{:15s}{:5s}'.format('Name','Score'))
                                #Reset game score
                                leaderboardscore = 10000
                                
                                #sort leaderboard list in ascending order
                                l = len(leaderboardprint_list) 
                                for i in range(0, l): 
                                        for j in range(0, l-i-1): 
                                                if (leaderboardprint_list[j][1] > leaderboardprint_list[j + 1][1]): 
                                                        tempo = leaderboardprint_list[j] 
                                                        leaderboardprint_list[j]= leaderboardprint_list[j + 1] 
                                                        leaderboardprint_list[j + 1]= tempo

                                #print in descending order
                                leaderboardprint_list.reverse()
                                for rank in range(len(leaderboardprint_list)):
                                        print('{:15s}{:5d}'.format(leaderboardprint_list[int(rank)][0],leaderboardprint_list[int(rank)][1]))

                                #end maze actions
                                #change input to uppercase
                                restartmazelowercase = input('Congratulation!! You have completed the maze.\nDo you want to restart maze? (\'N\' will send you back to the main menu) (Y/N):')
                                restartmaze = restartmazelowercase.upper()
                                if restartmaze == 'Y':
                                        restartplaymaze()
                                        viewmaze(filename)
                                elif restartmaze == 'N':
                                        restartplaymaze()
                                        mazemenu()
                                        break
                                else:
                                        print('Invalid Input. Please try again.')
                        #change input to uppercase
                        optionlowercase = input('\'W\' for UP, \'A\' for LEFT, \'S\' for DOWN, \'D\' for RIGHT, \'M\' for MAIN MENU, \'R\' to RESTART: ')
                        option = optionlowercase.upper()

                        #moving in maze & call function
                        if option == 'W':
                                playmaze(-1,0)
                                leaderboardscore -= 100
                        elif option == 'A':
                                playmaze(0,-1)
                                leaderboardscore -= 100
                        elif option == 'S':
                                playmaze(1,0)
                                leaderboardscore -= 100
                        elif option == 'D':
                                playmaze(0,1)
                                leaderboardscore -= 100
                        elif option == 'M':
                                mazemenu()
                                break
                        elif option == 'R':
                                restartplaymaze()
                                viewmaze(filename)
                        
#==============================================================================================================
#==============================================================================================================
        #configure maze
        elif select == 4:
                #print the maze and the option chosen
                print('Option [{}] Configure Current Maze\n\n========================================='.format(select))
                viewmaze(filename)

                #Configure the maze codes
                found = ''
                while True:
                        configmenu()
                        choice = int(input('Enter your options: '))
                        if choice == 1:
                                found = configcut('X')
                                if found[0] == True:
                                       continue
                                elif found[1] == True:
                                        mazemenu()
                                        break
                        elif choice == 2:
                                found = configcut('O')
                                if found[0] == True:
                                       continue
                                elif found[1] == True:
                                        mazemenu()
                                        break
                        elif choice == 3:
                                found = configcut('A')
                                if found[0] == True:
                                       continue
                                elif found[1] == True:
                                        mazemenu()
                                        break
                        elif choice == 4:
                                found = configcut('B')
                                if found[0] == True:
                                       continue
                                elif found[1] == True:
                                        mazemenu()
                                        break
                        elif choice == 5:
                                mazemenu()
                                break
                        else:
                                print('Invalid input, please try again.')
#==============================================================================================================
#==============================================================================================================
        #export maze
        elif select == 5:
                #print the option chosen and request input of the file name to save to
                print('Option [{}] Export Maze to file\n'.format(select))
                filesavename = input('Enter filename to save to: ')

                #exporting the maze and displaying the lines exported codes
                lineexport = 0
                try:
                        file = open(filesavename,'w')  
                        for row in maze_list:
                                joined=''.join(row)
                                file.write('{}\n'.format(str(joined)))
                                lineexport += 1
                        print('File {} created with {} record'.format(filesavename,lineexport))
                        file.close()
                except IOError:
                        print('Error, File name/type does not exist')
#==============================================================================================================
#==============================================================================================================
        #create new maze
        elif select == 6:
                #printing the option chosen
                print('Option [{}] Create New Maze\n'.format(select))

                #confirming the user want to rewrite the current maze
                while True:
                        emptymaze = input('This will empty the current maze. Are you sure? (Y or N): ')
                        if emptymaze == 'Y':
                                maze_list.clear()
                                dimension = input('Enter the dimension of the maze (row,column): ')
                                createnew = dimension.split(',')
                                for row in range(int(createnew[0])):
                                        newrow = []
                                        for col in range(int(createnew[1])):
                                                newrow.append('O')
                                        maze_list.append(newrow)
                                viewmaze(filename)
                        if emptymaze == 'N':
                                stopreplace = input('Return to Menu? (Y/N): ')
                                if stopreplace == 'Y':
                                        mazemenu()
                                        break
                                elif stopreplace == 'N':
                                        continue
                                else:
                                        print('Invalid Input, please try again')
#==============================================================================================================
#==============================================================================================================

#*****ONLY WORK IN RASPBERRY PI*****
#***********************************
        elif select == 7:
                from sense_hat import SenseHat
                from time import sleep
                sense = SenseHat()
                sense.clear()
                leaderboardprint_list = []
                leaderboardtemplist = []
                X=(255,255,255) #white
                O=(0,0,0) #black
                A=(255,0,0) #red
                B=(0,0,255) #green
                
                #replace the 'X','O','A' and 'B' into X,O,A and B in the list
                mazecombined = maze_list
                mazecombined = ",".join(repr(i) for i in mazecombined).replace("'","")
                maze_listpi = eval('[{}]'.format(mazecombined))

                #find location of A in the raspberry pi
                for row in range(len(maze_listpi)):
                        for col in range(len(maze_listpi[row])):
                                if maze_listpi[row][col]== A:
                                        mazeApospi = [row,col]

                #find location of B in the raspberry pi
                for row in range(len(maze_listpi)):
                        for col in range(len(maze_listpi[row])):
                                if maze_listpi[row][col]== B:
                                        mazeBpospi = [row,col]
                
                #Shows the Coordinate of A in the raspberry pi
                mazeviewlocationpi(A)

                #Shows the Coordinate of B in the raspberry pi
                mazeviewlocationpi(B)

                #set the leaderboardscore to 10000 and minus 100 every move taken
                leaderboardscore = 10000

                sense.set_pixels(sum(maze_listpi,[]))
                flag = True
                while flag:
                        if maze_listpi[int(mazeBpospi[0])][int(mazeBpospi[1])] == A:
                                #Leaderboard codes in the raspberry pi
                                playername = input('Your score is {}, please enter you name: '.format(leaderboardscore))
                                leaderboardtemplist = [playername,leaderboardscore]
                                leaderboardprint_list.append(leaderboardtemplist)
                                print('{:15s}{:5s}'.format('Name','Score'))
                                #Reset game score in the raspberry pi
                                leaderboardscore = 10000
                        
                                #sort leaderboard list by ascending order in the raspberry pi
                                l = len(leaderboardprint_list) 
                        for i in range(0, l): 
                                for j in range(0, l-i-1): 
                                        if (leaderboardprint_list[j][1] > leaderboardprint_list[j + 1][1]): 
                                                tempo = leaderboardprint_list[j] 
                                                leaderboardprint_list[j]= leaderboardprint_list[j + 1] 
                                                leaderboardprint_list[j + 1]= tempo

                        #print in descending order in the raspberry pi
                        leaderboardprint_list.reverse()
                        for rank in range(len(leaderboardprint_list)):
                                print('{:15s}{:5d}'.format(leaderboardprint_list[int(rank)][0],leaderboardprint_list[int(rank)][1]))

                        #end maze actions in the raspberry pi
                        #change input to uppercase in the raspberry pi
                        restartmazelowercase = input('Congratulation!! You have completed the maze.\nDo you want to restart maze? (\'N\' will send you back to the main menu) (Y/N):')
                        restartmaze = restartmazelowercase.upper()
                        if restartmaze == 'Y':
                                restartplaymazepi()
                                sense.set_pixels(sum(maze_listpi,[]))
                        elif restartmaze == 'N':
                                restartplaymazepi()
                                mazemenu()
                                break
                        else:
                                print('Invalid Input. Please try again.')
                
                #Detect joystick in the raspberry pi and change the LED lights accordingly
                for event in sense.stick.get_events():
                    if event.action == 'pressed':
                        if event.direction == 'up':
                            playmazepi(-1,0)
                            leaderboardscore -= 100
                            sense.set_pixels(sum(maze_listpi,[]))
                        elif event.direction == 'down':
                            playmazepi(1,0)
                            leaderboardscore -= 100
                            sense.set_pixels(sum(maze_listpi,[]))
                        elif event.direction == 'left':
                            playmazepi(0,-1)
                            leaderboardscore -= 100
                            sense.set_pixels(sum(maze_listpi,[]))
                        elif event.direction == 'right':
                            playmazepi(0,1)
                            leaderboardscore -= 100
                            sense.set_pixels(sum(maze_listpi,[]))
                        elif event.direction == 'middle':
                            flag = False
                            sense.set_pixels(sum(maze_listpi,[]))


                sense.set_pixels(sum(maze_listpi,[]))

#==============================================================================================================
#==============================================================================================================
        #View leaderboard
        elif select == 8:
                print('{:15s}{:5s}'.format('Name','Score'))
                for rank in range(len(leaderboardprint_list)):
                        print('{:15s}{:5d}'.format(leaderboardprint_list[int(rank)][0],leaderboardprint_list[int(rank)][1]))
                mazemenu()

#==============================================================================================================
#==============================================================================================================
        #end maze
        elif select == 0:
                break
        
        #invalid input at the main menu
        else:
                print('Invalid Input. Please try again')
                continue
