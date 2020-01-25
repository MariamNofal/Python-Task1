import sys
import os
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from arg_pars import parse_arg

def run(args):
    if args is None or len(args) == 0:
        print("No Directory specified")
        help()
        return
    
    farg, path = parse_arg(args)
    if path is None:
        print("No Directory specified")
        help()
        return
    logging.basicConfig(filename= farg,
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = os.path.expanduser(path)
    path = os.path.realpath(path)
    event_handler = LoggingEventHandler()
    observer = Observer()
    print(path, farg)
    try:
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
    except OSError:
        print("Wrong Path")
        sys.exit(-1)

    try:
        cmd = raw_input("Press r to return without exiting, Any other key to stop monitoring")
        if cmd == "r":
            return
    except KeyboardInterrupt:
        pass
    
    observer.stop()
    observer.join()


def help():
    print("*****Help page*****")
    print("Send path to directory to Monitor")

if __name__ == "__main__":
    run(raw_input())
    raw_input("waiting")
