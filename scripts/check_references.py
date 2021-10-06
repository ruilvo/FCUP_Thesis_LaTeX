import re, glob 
import os 

def main(paths):
    """
        Checks the provided paths to see if all labels are referenced

        paths: list with the paths to the Appendices and Chapters folders
    """
    if not isinstance(paths, (list, tuple)):
        raise Exception("Wrong input data type. Provide a list/tuple with the paths!")
    all_labels = {}
    all_refs   = {}

    for path in paths:
        x = glob.glob(os.path.join(path, '/*.tex'))

        for ff in x:
            with open(ff, mode = 'r') as file:
                for line in file:
                    if line.startswith("%"):
                        continue

                    split_label = line.split(r"\label{")
                    split_ref = line.split(r"\ref{")

                    if len(split_label) != 1:
                        
                        for lab in split_label[1:]:
                            this_label = lab.split('}')[0]

                            if this_label in all_labels:
                                print("WARNING: ", this_label, " defined more than once in file: ", ff)
                            else:
                                all_labels[this_label] = 0

                    if len(split_ref) != 1:
                        
                        for ref in split_ref[1:]:
                            this_ref = ref.split('}')[0]

                            try:
                                all_refs[this_ref] += 1
                            except KeyError as e:
                                all_refs[this_ref] = 1
        

    differences =  all_labels.keys() - all_refs.keys() 

    return differences if differences else "No differences between labels and refs"


if __name__ == '__main__':
    main([])