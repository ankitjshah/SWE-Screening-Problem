import json
from JsonFlatten import flatten, schemaValidation

# Reading from file
with open('testJson.json') as test:
  data = json.load(test)


with open('testSchema.json') as schema:
  testSchema = json.load(schema)
  

def runTest(data):
  for key in data["data"]:
    
    flatRecord ={}
    print(key['title'])

    flatRecord = flatten.FlattenJson(json.dumps(
    schemaValidation.validateJsonSchema(key['input'], testSchema)),'', flatRecord);
    if json.dumps(key['expectedOutput'])==json.dumps(flatRecord):
      print("PASS")
    else:
      print("FAIL")
    

runTest(data)