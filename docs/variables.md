## 5. Variables

### Single Declaration

```emer
var a = 10
var b(int) = 20
var name(str) = "Ada"
var empty
```

### Block Declaration

```emer
var {
  name(str)=("Ada"),
  age(int)=(20),
  active(bool)=(true)
}
```

### Assignment

```emer
var x = 1
x = x + 10
```

Index assignment is supported:

```emer
var xs = [1, 2, 3]
xs[1] = 99

var d = dict("a", 1)
d["b"] = 2
```
