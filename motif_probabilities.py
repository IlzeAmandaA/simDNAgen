
import os
import torch

class Motifs():

    def __init__(self, filepath):
        self.filenames = self.obtain_all_files(filepath)
        self.motifs = {}
        self.motif_generation()

        #load motifs of interest
    def obtain_all_files(self,filepath):
        """
            Returns all files for a specific folder that end in .txt
        """
        file_list = []
        for filename in os.listdir(filepath):
            if filename.endswith(".pfm"):
                file_list.append(os.path.join(filepath, filename))
                continue
            else:
                continue
        return file_list

    def motif_generation(self):
        for file in self.filenames:
            f = open(file)
            P_counts = []
            for i,line in enumerate(f):
                if i==0:
                    name = line.split(' ')[1]
                    name=name[:-1]
                    # print(name)
                else:
                    counts = []
                    for i in line.split(' '):
                        try:
                            counts.append(float(i))
                        except ValueError:
                            pass
                    P_counts.append(counts)
            P_counts = torch.tensor(P_counts, dtype=torch.float32)
            sum = P_counts.sum(dim=0)
            PPM = P_counts/sum
            # PPW = torch.log2((PPM/0.25))
            # PPW = PPW.permute(1,0) #convert to seq_idx X letter_prob
            self.motifs[name]=PPM.permute(1,0).numpy()




