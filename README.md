# ENAP
ENAP: An Efficient Number-Aware Pruning Framework for Design Space Exploration of Approximate Configurations

ENAP differs from the general search framework in that it performs a search space pruning before DSE, and it is the first to perform search space pruning from the perspective of constraining the number of approximation units, which
can improve the efficiency of DSE. The purpose of the ENAP technique is to ideally find the best set of approximate configurations to minimize energy consumption under the error constraint.

Requirements:

(1) The application needs to generate CDFG files through GAUT[1].

(2) Combine the CDFG file of the application to form the corresponding calculation function file (for example, applications/laplacecomputing. py).

Using ENAP:

(1) The applied CDFG file needs to be parsed through DFGparsing (open DFGparsing.py and replace the file name).

(2) Open GAmedcomputing.py, lines 32 and 36 need to be replaced according to the calculation function file.

(3) Open ENAP.py, select the error constraint and set the configuration parameters of the genetic algorithm.

(4) Run ENAP.py

[1] E. Martin, O. Sentieys, H. Dubois, and J. L. Philippe, “GAUT: Anarchitectural synthesis tool for dedicated signal processors,” in European
Design Automation Conference, 1993
