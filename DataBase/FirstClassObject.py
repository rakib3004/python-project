class IT_Room:
    computer=0

    def pcCounter(self):
        self.computer = self.computer+1
        print('Computer No',self.computer)


it_room = IT_Room()
it_room.pcCounter()
it_room.pcCounter()
it_room.pcCounter()