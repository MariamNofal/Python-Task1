import os

def parse_arg(args):
    argv = args.split(" ")
    fout = None
    fout_id = -1
    print(argv)
    try:
        argv.remove("-h")
    except ValueError:
        pass

    try:
        fout_id = argv.index("-o")
    except ValueError:
        pass
    print(fout_id)
    if fout_id >= 0:
        fout = argv[fout_id + 1]
        fout = os.path.expanduser(fout)
        fout = os.path.realpath(fout)
        del argv[fout_id]
        del argv[fout_id]
    print(argv)
    if (len(argv) > 0) :
        return fout, " ".join(argv)
    else:
        return fout, None
