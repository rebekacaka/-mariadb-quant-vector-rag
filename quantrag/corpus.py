#this function reads a text file and returns a Python list of the article titles in 

#this is the bridge between data_quant/corpus_titles.txt anf the code. Then the python code corpus knows which article to download. 
#since it does local file handling and not network access it is not part of fetch.py



def load_titles(path):
    titles = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):  #this is to skip lines which are not tittles 
                continue
            titles.append(line)
    return titles



