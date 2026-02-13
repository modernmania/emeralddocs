## 19. Example Program

```emer
var nums = [1, 2, 3, 4]
var squares = []

for(n in nums) {
  squares = append(squares, math_pow(n, 2))
}

print(f"squares = {squares}")
```
