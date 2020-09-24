
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    #raise NotImplementedError()
    content = []
    with open(csv_file_path, "r") as f:
        lines = f.readlines()        
        for line in lines:
            list_strings = line.split(",")
            list_vals = []
            for item in list_strings:
                try:
                    v = int(item)
                    list_vals.append(v)
                except ValueError:
                    try:
                        v = float(item)
                        list_vals.append(v)
                    except ValueError:
                        v = rem_quotes(item)
                        list_vals.append(v)
            content.append(list_vals)
    return content


def rem_quotes(item):
    return item.strip("\"")
    