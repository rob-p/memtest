#include <iostream>
#include <fstream>
#include <tuple>
#include <vector>

int main(int argc, char* argv[]) {
	
	std::ifstream ifile(argv[1]);
	std::vector< std::tuple<size_t, size_t> > edges;
	size_t a,b;
	while( ifile >> a >> b ) {
		edges.push_back( std::make_tuple(a,b) );
	}
	std::cerr << "there were " << edges.size() << " edges\n";
	ifile.close();
}