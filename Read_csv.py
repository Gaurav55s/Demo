def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []         #Create array.
    for item in data_line.strip().split(','):
        if item =='':
            values.append(0.0)
        else : 
            values.append(item)
    return values

def create_item_dict(values,headers):
    result = {}
    for value,header in zip(values,headers):
        result[header] = value
    return result

def read_csv(path):
    result1 = []
    #Open the file in read mode
    with open(path,'r') as f:
        #Get a list of lines
        lines = f.readlines()
        #Parse the header
        headers_1 = parse_headers(lines[0])
        #Loop over the remaining lines
        for data_line in lines[1:]:
            #Parse the values
            values_1 = parse_values(data_line)
            #Create a dictionary using values & headers
            item_dict = create_item_dict(values_1,headers_1)
            #Add the dictionary to the result
            result1.append(item_dict)
    return result1