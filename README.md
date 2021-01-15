# Pelmorex Corp - SWE Screening Problem

The JSON request object has been verified against the available schema.
You can find the source code at [Github](https://github.com/ankitjshah/SWE-Screening-Problem.git).

## Prerequisite

Use the  [Python v3.0](https://www.python.org/download/releases/3.0/).

## Test
Execute the below command to run all the test cases

```bash
python validate.py
```

## Additional considerations

- Except [json](https://docs.python.org/3/library/json.html), no other library has been used in this assignment.

- However, the use of libraries such as [re](https://docs.python.org/3/library/re.html) would have been recommended for the string format validation.

For ex.,
```python
def validateSizeFormat(size):
    if size.find('x') != -1:
        size = size.split('x', 1)
        if len(size) == 2 and size[0].isnumeric() and size[1].isnumeric():
            return True
        else:
            return False
    else:
        return False
```

The above code could be reduced to just 2 lines with the use of [re](https://docs.python.org/3/library/re.html). As shown below:

```python
re.search("^([\\d.]+)x([\\d.]+).*$", record[key])  
```

- There is a total of four test cases included to validate the structure of the incoming JSON object.

   1. Test case for extra key
   2. Test case for the invalid default value
   3. Test case for the invalid type of key
   4. Test case for the actual JSON object

## Special mention
It has been a great opportunity to be a part of Pelmorex's screening process. The assignment was really brainstorming and helped me to use the different concepts in a single program.

## License
This assignment was created as part of a screening process for [Pelmorex Corp](https://www.pelmorexsolutions.com/contact-us/). 