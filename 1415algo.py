
'''
-----------------
| 1 | 2 | 3 | 4 |
-----------------
| 5 | 6 | 7 | 8 |
-----------------
| 9 |10 |11 |12 |
-----------------
|13 |14 |15 |   |
-----------------
{1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12', 13:'13', 14:'14', 15:'15', 16:' '}

'''

class algo():

    def __init__(self):

        self.posSet = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 
                       9:'9', 10:'10', 11:'11', 12:'12', 13:'13', 14:'14', 15:'15', 16:' '}
        self.moves = {'u':True, 'd':True, 'l':True, 'r':True}

    def isValid(self):
        '''Illegal conditions: if pos-4 < 0, bottom edge, if pos+4 is IndexError, top edge, if pos%4 = 0, right side, if (pos-1)%4 = 0 left side'''

        # First, Identify the position of the blank space.
        for i in self.posSet:
            if self.posSet[i] == ' ':
                self.blankPos = i


        # Is moving down an invaild move
        # try:
        #     tmp = self.posSet[self.blankPos + 4]
        # except:
        #     the_type = sys.exc_info()
        #     if the_type == IndexError:
        #         self.down = False
        #     else:
        #         print(f'bruh this error wasn\'t supposed to happen: {the_type}')

        # # Is moving up an illegal move
        # if self.blankPos - 4 < 0:
        #     self.up = False
        # else:
        #     pass

        # # Is moving left an illegal move
        # if not self.blankPos - 1 % 4:
        #     self.left = False

        # # Is moving right an illegal move
        # if not self.blankPos % 4:
        #     self.right = False



    def checkUserMove(self):
        self.userMove = input('Your move...\n>>> ').lower()[0]
        if not self.userMove in self.moves:
            print('Not a valid option.')

        if isValid( self.moves[ self.userMove ] ):
            self.moveAndDisplay()

    def moveAndDisplay(self):

        # Move bit:



        # Display bit:
        counter = 1
        while counter < 16:

            if counter % 4 == 0:
                print('\n-----------------')
            if len(self.posSet[counter]) == 2:
                print(f'|{self.posSet[counter]} ', end='') 
            else:
                print(f'| {self.posSet[counter]} ', end='')



            counter += 1

a = algo()
a.moveAndDisplay()





