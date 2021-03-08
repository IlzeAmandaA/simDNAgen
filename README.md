# simDNAgen: Simulate DNA data with motifs (short 'relevant' sequences) 
The repository contains python code to generate 'fake' DNA sequences of different lengths, based on the underlying known statistics of DNA data. For a more detailed explanation read section 4.1 of the `report.pdf` that can be found here: [repo](https://github.com/IlzeAmandaA/BayesianCNN-DNA)

## How to use
motifs directory
- store the target motif position probability matrix (PPM) files. This matrix represents the probability of each letter at a given position of a motif.

root directory
- generate.py: generates a position probability matrix for each motif listed in the motifs directory

- motif_probabilities.py : generates DNA sequences as txt files and stores them in output. In this file you can define the number of squences to be generated, as well as their length. 
