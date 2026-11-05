def load_titles(path):
    titles = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            titles.append(line)
    return titles