# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
import sys
import resource

def main():
    fn = sys.argv[1]
	edges = []
	with open(fn) as ifile:
    for l in ifile:
        toks = l.rstrip().split()
        edges.append( (int(toks[0]), int(toks[1])) )

    print("There were {0} edges".format(len(edges)))
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("Memory usage was {0}".format(mem))

if __name__ == "__main__":
	main()
