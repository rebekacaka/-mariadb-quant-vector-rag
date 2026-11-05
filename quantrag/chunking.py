import re

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

def make_chunks(paragraphs, max_words):
    chunks = []
    current = []
    count = 0
    for paragraph in paragraphs:
        n = len(paragraph.split())
        if count + n > max_words and current:
            chunks.append("\n\n".join(current))
            current = []
            count = 0
        current.append(paragraph)
        count = count + n
    if current:
        chunks.append("\n\n".join(current))
    return chunks

def split_long_paragraphs(paragraphs, max_words):
    result = []
    for paragraph in paragraphs:
        if len(paragraph.split()) > max_words:
            result.extend(re.split(r"(?<=[.!?])\s+", paragraph))
        else:
            result.append(paragraph)
    return result

#carry the current heading as a running variable instead of building a full section tree,
#because it's simple and enough to prefix each chunk with Title > Section, at the cost of losing the nesting of subsections.

def sectioned_paragraphs(text):
    heading = "Introduction"
    result = []
    for block in text.split("\n\n"):
        lines = block.strip().split("\n")
        while lines and lines[0].startswith("=="):
            heading = lines[0].strip("= ")
            lines = lines[1:]
        body = "\n".join(lines).strip()
        if body != "":
            result.append((heading,body))
    return result


SKIP_SECTIONS = {"References", "External links", "See also", "Further reading",
                 "Notes", "Sources", "Bibliography"}


def chunk_article(title, text, max_words):
    text = clean_formulas(text)
    sections = []
    for heading, paragraph in sectioned_paragraphs(text):
        if heading in SKIP_SECTIONS:
            continue
        if sections and sections[-1][0] == heading:
            sections[-1][1].append(paragraph)
        else:
            sections.append((heading, [paragraph]))
    chunks = []
    for heading, paragraphs in sections:
        paragraphs = split_long_paragraphs(paragraphs, max_words)
        for piece in make_chunks(paragraphs, max_words):
            chunks.append({
                "title": title,
                "section": heading,
                "text": title + " > " + heading + "\n\n" + piece,
            })
    return chunks


