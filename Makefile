GenEdges: all.txt
	python GenEdges.py 44720000 all.txt

ReadGraphs: ReadGraphs.cpp
	g++ -std=c++11 -o ReadGraphs ReadGraphs.cpp
