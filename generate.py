import random
import numpy as np
from scipy.stats import poisson
from motif_probabilities import Motifs

#18 genes
# ACGT = 0.25 probability
#create 18 reference genes
keys = ['a', 'c', 'g', 't']
probabilties = [0.25, 0.25, 0.25, 0.25]
people_count=160
output_dict = 'output/'

motifs = Motifs('motifs')


genes={}
lenghts = [25370, 47402, 84651, 33734, 30160,
           2980, 18541, 98820, 32188,
           3353, 5415, 3736, 3180, 7038,
           21693, 3065, 3108, 4176]


for idx,n in enumerate(lenghts):
    print('Gene selected ', idx)
    gene=list(''.join(np.random.choice(keys, n, replace=True, p=probabilties)))
    if idx>=9:
        #generate random mutations
        for person in range(people_count):
            for mutatation in range(int(len(gene)*0.01)):
                m=random.randint(0, len(gene)-1)
                gene[m]=np.random.choice(keys, 1, replace=True, p=probabilties)[0]

            label = 0 if person < 80 else 1
            f=open(output_dict+'person'+str(person)+'.txt', 'a')
            f.write('chrom' + str(idx) + ',' + ''.join(gene) + ',' + str(label) + '\n')
            f.close()


    else:
        #insert motifs based on poisson distribution
        num_average = int((n * 0.055) / 11)
        num_poisson = poisson(num_average, loc=int(n / 3000)).rvs()
        # print(num_average, num_poisson)
        gene_orig=gene.copy()

        for person in range(people_count):
            if person>=80:
                label=1
                gene = gene_orig.copy()
                used_idx=[]
                for insertion in range(num_poisson): #number of insterstions needed
                    m = random.randint(0, len(gene)-12) #random location
                    while m in used_idx:
                        m = random.randint(0, len(gene)-12)

                    if idx<3:
                        ppm_motif = motifs.motifs['NRF1']
                    elif idx>=3 and idx<6:
                        ppm_motif = motifs.motifs['TFAP2A']
                    else:
                        motif= ['NRF1','TFAP2A'][random.randint(0,1)]
                        ppm_motif=motifs.motifs[motif]

                    for i_n,n in enumerate(range(len(ppm_motif))): #selected motif length
                        letter = np.random.choice(keys, 1, replace=True, p=ppm_motif[i_n])[0]
                        gene[m+i_n] = letter
                        used_idx.append(m+i_n)

            else:
                label=0
                for mutatation in range(int(len(gene) * 0.01)):
                    m = random.randint(0, len(gene) - 1)
                    gene[m] = np.random.choice(keys, 1, replace=True, p=probabilties)[0]

            f = open(output_dict+'person' + str(person) + '.txt', 'a')
            f.write('chrom' + str(idx) + ',' + ''.join(gene) + ',' + str(label) + '\n')
            f.close()
