def write_to_file(file,data):
    with open(file,"w",encoding="utf-8") as f:
        f.write(data)