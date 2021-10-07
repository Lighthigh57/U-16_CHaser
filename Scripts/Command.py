import CHaser

class Command():
    """
    各種行動を起こします。
    """
    run = None
    ready_OK = False

    def __init__(self):
        global run
        run = CHaser.Client()
        """set instance"""

    def move(self,com, dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """
        global run
        global ready_OK

        if ready_OK == False: #if didn't get_ready()
            self.get_ready()
            print("Warning!:You didn't get_ready().")

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
        ready_OK = False

        return result

    def get_ready(self):
        """Lunch get_ready and return map."""
        global run
        global ready_OK

        ready_OK = True
        return run.get_ready()
