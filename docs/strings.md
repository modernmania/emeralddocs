## 7. String Interpolation (f-strings)

Use `f"..."` with `{expr}`:

```emer
var name = "Ada"
var n = 5
print(f"Hello {name}, n={n}, sum={n+1}")
```

Interpolation compiles to string concatenation behavior.

## 8. Statements

### print

```emer
print("Hello")
print(1 + 2)
```

### input

Modern forms:

```emer
var a = input()
var b = input("Name: ")
var c = read("Prompt: ")  # alias
```

Legacy form is still accepted:

```emer
input(plc("Name: "))
```

### wait

```emer
wait(500)  # milliseconds
```

### check

Fails at runtime if expression is falsy:

```emer
check 1 == 1
check len([1]) > 0
```

### return

```emer
return
return 42
```
