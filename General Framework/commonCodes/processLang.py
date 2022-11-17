def dataProcess(full_data, keyword):
    keywords = keyword.split('][')
    keywords[0] = keywords[0].split('[')[1]
    keywords[-1] = keywords[-1].split(']')[0]
    output = full_data.copy()  

    for key in keywords:
        output = output[key]
        if type(output)  == list:
            output = output[0]
    return output

def dataProcess_with_label(full_data, keyword):
    keywords = keyword.split('][')
    keywords[0] = keywords[0].split('[')[1]
    keywords[-1] = keywords[-1].split(']')[0]
    output = full_data.copy()  

    for key in keywords:
        output = output[key]
        if type(output)  == list:
            output = output[0]
        label = key
    return output, label
