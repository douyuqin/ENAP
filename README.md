# ENAP
Requirements:
(1) The application needs to generate CDFG files through GAUT[1].
(2) Combine the CDFG file of the application to form the corresponding calculation function file (for example, applications/laplacecomputing. py).
Using ENAP:
(1) The applied CDFG file needs to be parsed through DFGparsing (open DFGparsing.py and replace the file name).
(2) Open GAmedcomputing.py, lines 32 and 36 need to be replaced according to the calculation function file.
(3) Open ENAP.py, select the error constraint and set the configuration parameters of the genetic algorithm.
(4) Run ENAP.py
