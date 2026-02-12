## 9. Control Flow

### if / else if / else

```emer
if(x > 10) {
  print("big")
} else if(x == 10) {
  print("equal")
} else {
  print("small")
}
```

### while

```emer
while(x < 5) {
  x = x + 1
}
```

### for(condition)

```emer
for(true) {
  print("loop")
  brk
}
```

### for-in

```emer
var xs = [10, 20, 30]
for(item in xs) {
  print(item)
}
```

### Loop control

```emer
brk   # break
cont  # continue
```
