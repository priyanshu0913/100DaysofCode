[![Imgur](https://i.imgur.com/Mz7sx3d.png)](https://replit.com/@priyanshu0913/100-Days-of-Code#Day%2001)

# Python print() Function

The `print()` function prints the specified message to the screen, or other standard output device.

The message can be a string, or any other object, the object will be converted into a string before written to the screen.

# Syntax

```
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

# Example

### Python Code

```python
print("Hello World")
```
### Output

```
Hello World
```

# Parameter Values 

| Parameter   | Description |
| ----------- | ----------- |
| *object(s)* | Any object, and as many as you like. Will be converted to string before printed |
| *sep='seperator'* | Specify how to separate the objects, if there is more than one. Default is ' ' |
| *end* | Specify what to print at the end. Default is '\n' (line feed) |
| *file* | An object with a write method. Default is sys.stdout |
| *flush* | A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False | 



# Python input() Function

The `input()` function allows user input.

# Syntax

```
input(prompt)
```
# Example

### Python Code

```python
name = input("Enter your name : ")
print(name)
```
### Output

```
Enter your name : Priyanshu
Priyanshu
```

# Parameter Values 

| Parameter   | Description |
| ----------- | ----------- |
| *prompt* | A String, representing a default message before the input. |