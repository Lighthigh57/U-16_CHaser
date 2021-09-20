from random import triangular
import CHaser

class Command:
    run = None
    infoOK = None

    def __init__(self):
        global run
        global infoOK
        
        infoOK = False
        run = CHaser.Client()

    def move(self, com,dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """
        global run
        global infoOK
        if infoOK == False:
            self.get_info()
            print("Warning!:You didn't get_info().")

        if com == "put":
            if dir == 1:
                run.put_up()
                
            if dir == 7:
                run.put_down()
                
            if dir == 3:
                run.put_left()
                
            if dir == 5:
                run.put_right()
                
        if com == "walk":
            if dir == 1:
                run.walk_up()
                
            if dir == 7:
                run.walk_down()
                
            if dir == 3:
                run.walk_left()
                
            if dir == 5:
                run.walk_right()
                
        if com == "look":
            if dir == 1:
                run.look_up()
                
            if dir == 7:
                run.look_down()
                
            if dir == 3:
                run.look_left()
                
            if dir == 5:
                run.look_right()
                
        if com == "search":
            if dir == 1:
                run.search_up()
                
            if dir == 7:
                run.search_down()
                
            if dir == 3:
                run.search_left()
                
            if dir == 5:
                run.search_right()
        
        print(com+" "+str(dir))
        infoOK = False
    
                
        

    def get_info(self):
        global run
        global infoOK

        infoOK = True
        return run.get_ready()

