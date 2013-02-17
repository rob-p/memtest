memtest 
=======

This simple test code accompanies the blog post [here](http://robpatro.com/blog/?p=168).
To generate the input file, just use `make GenEdges`.  This will create a file `all.txt`. 
You can then run the Python implementation with `python ReadGraphs.py all.txt`.  To 
compile the C++ version, use `make ReadGraphs` and run it with `ReadGraphs all.txt`.
