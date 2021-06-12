import json
correct_json = '{"name":"john","age":30}'
try:
         a_json = json.loads(correct_json)
         print(a_json)
except json.decoder.JSONDecodeError:
         print("String could not be printed")
