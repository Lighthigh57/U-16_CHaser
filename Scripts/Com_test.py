import Command

runner = None

def main():
    """
    実行するやつ
    """
    global runner
    while True:
        runner.get_info()
        runner.move("walk",7)

if __name__ == "__main__":
    runner = Command.Command()
    main()