import CHaser

class Command:
    run = None
    def __init__(self):
        global run

        run = CHaser.Client()

    def move(self, com,dir):
        global run

        if com == "put":
            if dir == 1:
                run.put_up()
                pass
            if dir == 7:
                run.put_down()
                pass
            if dir == 3:
                run.put_left()
                pass
            if dir == 5:
                run.put_right()
                pass
        if com == "walk":
            if dir == 1:
                run.walk_up()
                pass
            if dir == 7:
                run.walk_down()
                pass
            if dir == 3:
                run.walk_left()
                pass
            if dir == 5:
                run.walk_right()
                pass
        if com == "look":
            if dir == 1:
                run.look_up()
                pass
            if dir == 7:
                run.look_down()
                pass
            if dir == 3:
                run.look_left()
                pass
            if dir == 5:
                run.look_right()
                pass
        if com == "search":
            if dir == 1:
                run.search_up()
                pass
            if dir == 7:
                run.search_down()
                pass
            if dir == 3:
                run.search_left()
                pass
            if dir == 5:
                run.search_right()
                pass
        
        pass
    def get_info(self, parameter_list):
        global run

        return run.get_ready

