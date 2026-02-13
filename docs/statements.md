## 10. Statements

### print

```emer
print("Hello")
print(1 + 2)
```

### input / read

```emer
var a = input()
var b = input("Name: ")
var c = read("Prompt: ")
```

Legacy form supported:

```emer
input(plc("Name: "))
```

### wait

```emer
wait(500)
```

### check

```emer
check 1 == 1
check len([1]) > 0
```

### return

```emer
return
return 42
```
