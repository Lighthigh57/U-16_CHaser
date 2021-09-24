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

        result = []

        if infoOK == False:
            self.get_info()
            print("Warning!:You didn't get_info().")

        if com == "put":
            if dir == 1:
                result = run.put_up()
                
            if dir == 7:
                result = run.put_down()
                
            if dir == 3:
                result = run.put_left()
                
            if dir == 5:
                result = run.put_right()
                
        if com == "walk":
            if dir == 1:
                result = run.walk_up()
                
            if dir == 7:
                result = run.walk_down()
                
            if dir == 3:
                result = run.walk_left()
                
            if dir == 5:
                result = run.walk_right()
                
        if com == "look":
            if dir == 1:
                result = run.look_up()
                
            if dir == 7:
                result = run.look_down()
                
            if dir == 3:
                result = run.look_left()
                
            if dir == 5:
                result = run.look_right()
                
        if com == "search":
            if dir == 1:
                result = run.search_up()
                
            if dir == 7:
                result = run.search_down()
                
            if dir == 3:
                result = run.search_left()
                
            if dir == 5:
                result = run.search_right()
        
        print(com+" "+str(dir))
        infoOK = False

        return result
    
                
        

    def get_info(self):
        global run
        global infoOK

        infoOK = True
        return run.get_ready()

