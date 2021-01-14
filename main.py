import json
from JsonFlatten import flatten, validate

flatRecord = {}

# Reading from file
with open('sampleJson.json') as sampleJson:
  data = json.load(sampleJson)
# print(data)

with open('testSchema.json') as schemaJson:
  schema = json.load(schemaJson)


# Driver code
print(json.dumps(flatten.FlattenJson(json.dumps(
validate.validateJsonSchema(data, schema)),'', flatRecord)));
