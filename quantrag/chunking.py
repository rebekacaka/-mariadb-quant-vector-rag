#this function 


def split_paragraphs(text):
    paragraphs=[]
    for block in text.split("\n\n"): #here split the article into separate chunks evertime it sees two consecutive newline which is how paragraphs are achieved in plain text 
        block=block.strip() #Strips away any leftover leading or trailing spaces, tabs, or single line breaks 
                            #from both ends of each paragraph block so wont save any whitespace only strings. 

        if block == "" or block.startswith("=="):
            continue 
        paragraphs.append(block)
    return paragraphs

#this funtion makes sure to keep formulas clean and intact. AFter formulas are retrieved from Wikipedia, they tend to split into different single lines one after another 
#hence using a variable run to keep in check how many bad/shot lines pass by in a row and also using a cruical post loop 
#cheek helps us fix if the article ends with a mathematical equation the final if run>=3 outside the loop ensures the trailing "[formula]" merker still gets added before returning  
def clean_formulas(text):
    kept = []
    run = 0
    for line in text.split("\n"):
        if len(line.strip()) <= 3:
            run = run + 1
        else:
            if run >= 3:
                kept.append("[formula]")
            elif run > 0:
                kept.append("")
            run = 0
            kept.append(line)
    if run >= 3:
        kept.append("[formula]")
    return "\n".join(kept)
