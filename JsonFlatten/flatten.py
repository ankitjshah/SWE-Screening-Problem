import json
def generateName(name, x):
    if (name == ''):
        return x
    else:
        return name + '.' + x


def FlattenJson(y, name, flatJson):
    dictRecord = json.loads(y)

    key = dictRecord.keys()

    for x in list(key):
        if type(dictRecord[x]) is dict:
            FlattenJson(json.dumps(dictRecord[x]), name + x, flatJson)
        elif type(dictRecord[x]) is list:
            my_array = []
            for a in dictRecord[x]:
                if (type(a) is dict):
                    tempJson = {}
                    FlattenJson(json.dumps(a), '', tempJson)
                    my_array.append(tempJson)
                else:
                    my_array.append(a)
            flatJson[generateName(name, x)] = my_array
        else:
            flatJson[generateName(name, x)] = dictRecord[x]
    return flatJson
