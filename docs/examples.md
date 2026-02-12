## 16. Examples

```emer
var nums = [1, 2, 3, 4]
var squares = []

for(n in nums) {
  squares = append(squares, math_pow(n, 2))
}

print(f"squares = {squares}")

fnc findFirstBig(xs(list), threshold(int)) (int) {
  for(v in xs) {
    if(v > threshold) {
      return v
    }
  }
  return -1
}

print(findFirstBig(squares, 10))
```

```emer
print("Hello world!")
```
