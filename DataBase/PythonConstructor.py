class IT_Room:
    computer=0

    def __init__(self):
        print('New Object!!!!!!')

    def pcCounter(self):
        self.computer = self.computer+1
        print('Computer No',self.computer)

    def __del__(self):
     print('Object Broken??????')


it_room = IT_Room()
it_room.pcCounter()
it_room.pcCounter()
it_room.pcCounter()
it_room=5407
print('ID is:',it_room)