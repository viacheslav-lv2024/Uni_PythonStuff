length = float(input("Length (meters): "))
width = float(input("Width (meters): "))
height = float(input("Height (meters): "))
circumference = (length + width) * 2
volume = length * width * height
wall_area = height * 2 * (length + width)
n_of_windows = int(wall_area / 12)
painted_area = wall_area - n_of_windows * 2
needed_paint = 0.75 * painted_area
print(f"""Circumference: {circumference:.2f} meters
Volume: {volume:.2f} cubic meters
Wall area: {wall_area:.2f} square meters
Number of windows: {n_of_windows}
Needed paint: {needed_paint:.2f} liters""")
