import sys
import random

def redge():
	return (random.randint(0,4000), random.randint(0,4000))

def main():
	nedge = int(sys.argv[1])
	ofname = sys.argv[2]

	with open(ofname,'wb') as ofile:
		for i in xrange(nedge):
			ofile.write('{0[0]}\t{0[1]}\n'.format(redge()))

if __name__ == "__main__":
	main()