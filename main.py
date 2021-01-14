import json
# import sys
# sys.path.insert(0, './JsonFlatten')
from JsonFlatten import flatten, validate
# from validate.py import validateJsonSchema

flatRecord = {}

# typeArr = {
#     "App": {
#         "Name":{"typeVal":""},
#         "BundleID": {"typeVal":""},
#         "Categories": {
#           "defaultValues":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
#           "typeVal":[]
#           },
#     },
#     "Device": {
#         "OS": {
#           "defaultValues":["iOS","Android"],
#           "typeVal":""
#           },
#         "OSVersion": {"typeVal":""},
#     },
#     "AdSlots": [{
#         "Type":{
#           "defaultValues":["iOS","Android"],
#           "typeVal":""
#           },
#         "Banner":{"typeVal":""},
#         "Size": {"typeVal":"", "format":"^([\d.]+)x([\d.]+).*$"},
#         "Position": {"typeVal":""},
#         "PrivateDeal": {
#             "PriceCPM": {"typeVal":0.0},
#             "AuctionType": {"typeVal":0},
#             "ID":{"typeVal":""},
#         }
#     }, {
#         "Type": {"typeVal":""},
#         "Size": {"typeVal":"", "format":"^([\d.]+)x([\d.]+).*$"},
#         "Position": {"typeVal":""},
#         "Duration": {"typeVal":0},
#     }]
# }


# Handling App Object Value Error
# def validateJsonSchema(record, typeArr):
#     for key in list(record):
#         if key in typeArr:
#           if 'typeVal' not in typeArr[key]:
#             if type(record[key]) == type(typeArr[key]):
#               if type(record[key]) == dict:
#                   validateJsonSchema(record[key], typeArr[key])
#               elif type(record[key]) == list:
#                   for a in range(len(record[key])):
#                     if type(record[key][a]) == dict:
#                       validateJsonSchema(record[key][a], typeArr[key][0])
#               else: 
#                   record[key] = "null"
#           else:
#               if type(typeArr[key]['typeVal']) == type(record[key]):
#                 if 'defaultValues' in typeArr[key]:
#                   if record[key] in typeArr[key]['defaultValues']:
#                     continue
#                   else:
#                     record[key] = None
#                 if 'format' in typeArr[key]:
#                   # match variable contains a Match object.
#                   match = re.search(typeArr[key]['format'], record[key]) 

#                   if match:
#                     continue
#                   else:
#                     record[key] = None
#               else:
#                 record[key] = None
#         else:
#             del record[key]
#     return record

# def generateName(name, x):
#     if (name == ''):
#         return x
#     else:
#         return name + '.' + x


# def FlattenJson(y, name, flatJson):
#     dictRecord = json.loads(y)

#     key = dictRecord.keys()

#     for x in list(key):
#         if type(dictRecord[x]) is dict:
#             FlattenJson(json.dumps(dictRecord[x]), name + x, flatJson)
#         elif type(dictRecord[x]) is list:
#             my_array = []
#             for a in dictRecord[x]:
#                 if (type(a) is dict):
#                     tempJson = {}
#                     FlattenJson(json.dumps(a), '', tempJson)
#                     my_array.append(tempJson)
#                 else:
#                     my_array.append(a)
#             flatJson[generateName(name, x)] = my_array
#         else:
#             flatJson[generateName(name, x)] = dictRecord[x]
#     return flatJson


# JSON file
# data1 = '''{
# 	"App": {
# 		"Name": "Words with Friends",
# 		"BundleID": "com.zynga.words",
# 		"Categories": ["1", "3", "15"],
# 		"Category": [1, 3, 15]
# 	},
# 	"Device": {
# 		"OS": "Android",
# 		"OSVersion": "Jellybean"
# 	},
# 	"AdSlots": [
# 		{
# 			"Type": "Banner",
# 			"Size": "320x50",
# 			"Position": "0",
# 			"PrivateDeal": {
# 				"PriceCPM": 2.2,
# 				"AuctionType": 1,
# 				"ID": "abc"
# 			}
# 		},
# 		{
# 			"Type": "video",
# 			"Size": "320x'50'",
# 			"Position": "1",
# 			"Duration": 15
# 		}
# 	],
#   "hello": {
#     "hi":"how are yoi?"
#   }
# }'''

# Reading from file
with open('sampleJson.json') as sampleJson:
  data = json.load(sampleJson)
# print(data)

with open('testSchema.json') as schemaJson:
  schema = json.load(schemaJson)


# Driver code
# FlattenJson(json.dumps(
# handleAppSubObj(json.loads(data), typeArr)),'', flatRecord)
# FlattenJson(data,'', flatRecord)
print(json.dumps(flatten.FlattenJson(json.dumps(
validate.validateJsonSchema(data, schema)),'', flatRecord)));
