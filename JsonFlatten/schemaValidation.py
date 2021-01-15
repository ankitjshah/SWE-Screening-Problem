def validateJsonSchema(record, typeArr):
    for key in list(record):
        if key in typeArr:
            if 'typeVal' not in typeArr[key]:
                if type(record[key]) == type(typeArr[key]):
                    if type(record[key]) == dict:
                        validateJsonSchema(record[key], typeArr[key])
                    elif type(record[key]) == list:
                        for a in range(len(record[key])):
                            if type(record[key][a]) == dict:
                                validateJsonSchema(record[key][a],
                                                   typeArr[key][0])
                    else:
                        record[key] = "null"
            else:
                if type(typeArr[key]['typeVal']) == type(record[key]):
                    if 'defaultValues' in typeArr[key]:
                        if type(record[key]) == list:
                          for a in record[key]:
                            if a in typeArr[key]['defaultValues']:
                                continue
                            else:
                                record[key] = None
                        else:
                            if record[key] in typeArr[key]['defaultValues']:
                                continue
                            else:
                                record[key] = None
                    if 'format' in typeArr[key]:
                        # match variable contains a Match object.
                        match = validateSizeFormat(record[key])
                        if match:
                            continue
                        else:
                            record[key] = None
                else:
                    record[key] = None
        else:
            del record[key]
    return record


def validateSizeFormat(size):
    if size.find('x') != -1:
        size = size.split('x', 1)
        if len(size) == 2 and size[0].isnumeric() and size[1].isnumeric():
            return True
        else:
            return False
    else:
        return False
