import sys
from arg_pars import parse_arg

def run(args):
	farg, link= parse_arg(args)
	print(farg, link)
	if farg is not None:
		sys.stdout = open(farg, 'w')
	if (link is None) or (len(link)==0):
		help()
		return
	lst_output = _open_logs(link)
	_parse_logs(lst_output)



def help():
	print("help Page")
	print("please enter valid file Name or file path with the commade ")


def _open_logs(file):
	try:
	    f = open(file, 'r')
	    lst_lines = f.readlines()
	    lst_output = []
	    for log in lst_lines:
	        lst_output.append(log.split())
	    return lst_output
	except IOError:
		print("can't open this file")
		sys.exit()


def _parse_logs(lst_output):
    
    for log in lst_output:
        ip=log[0]
        access_methods=log[5][1:]
        uri=log[6]
        user_agent=(' '.join(log[11:-1]))
        print(" IP: "+ip)
        print(" Access Method: "+access_methods+"\n"+" URI: "  + uri)
        print(" UserAgents: "+ user_agent)
        print("")