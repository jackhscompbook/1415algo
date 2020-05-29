
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

import sys

class algo():

    def __init__(self):

        self.posSet = {1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 
                       9:'09', 10:'10', 11:'11', 12:'12', 13:'13', 14:'14', 15:'15', 16:'  '}

        self.moves = ['u', 'd', 'l', 'r']

    def isValid(self, move):
        '''Illegal conditions: if pos-4 < 0, bottom edge, if pos+4 is IndexError, top edge, if pos%4 = 0, right side, if (pos-1)%4 = 0 left side'''

        # First, Identify the position of the blank space.
        for i in self.posSet:
            if self.posSet[i] == '  ':
                self.blankPos = i

        #print('A')

        # Is moving down an invaild move
        try:
            tmp = self.posSet[self.blankPos + 4]
            #print(tmp)
        except KeyError as e:
            if move == 'd':
                return False
            else:
                pass

        #print('b')

        # Is moving up an illegal move
        if self.blankPos - 4 < 0 and move == 'u':
            return False
        #print('c')
        # Is moving left an illegal move
        # print(f'self.blankPos = {self.blankPos}')
        # print(f'self.blankPos - 1 = {self.blankPos - 1}')
        # print(move == 'l')
        # print(self.blankPos - (1 % 4 == 0 and move == 'l')
        if (self.blankPos - 1) % 4 == 0 and move == 'l':
            return False
        #print('d')
        # Is moving right an illegal move
        if self.blankPos % 4 == 0 and move == 'r':
            return False
        #print('e')
        if move not in self.moves:
            return False
        return True


    def swap(self, a, b): # this swaps 2 values in a dict. a, b are the keys of the items

        #print(self.posSet)
        
        self.posSet[a], self.posSet[b] = self.posSet[b], self.posSet[a]

        #print(self.posSet)


    def moveAndDisplay(self):
        while True:
            #display
            try:
                print(f'Your Move: {self.userMove}\n')
            except AttributeError as e:
                print('Game start.\n')
            print(f'''
            ---------------------
            | {self.posSet[1]} | {self.posSet[2]} | {self.posSet[3]} | {self.posSet[4]} |
            ---------------------
            | {self.posSet[5]} | {self.posSet[6]} | {self.posSet[7]} | {self.posSet[8]} |
            ---------------------
            | {self.posSet[9]} | {self.posSet[10]} | {self.posSet[11]} | {self.posSet[12]} |
            ---------------------
            | {self.posSet[13]} | {self.posSet[14]} | {self.posSet[15]} | {self.posSet[16]} |
            ---------------------
            ''')

            # Move bit:
            self.userMove = input('Your move...\n>>> ').lower()[0]
            valid = False
            #print(self.isValid(self.userMove))
            #print(self.userMove)

            if self.userMove == 'e':
                break

            if self.isValid(self.userMove):

                if self.userMove == 'u':
                    self.moveKey = self.blankPos - 4
                elif self.userMove == 'd':
                    self.moveKey = self.blankPos + 4
                elif self.userMove == 'l':
                    self.moveKey = self.blankPos - 1
                elif self.userMove == 'r':
                    self.moveKey = self.blankPos + 1


                self.swap(self.blankPos, self.moveKey)

            else:
                print('Invalid Option')

    def userPlay(self):

        print('User Play Starting.')
        self.moveAndDisplay()
        print('User Play Ending')



a = algo()
a.userPlay()





