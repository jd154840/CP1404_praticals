COLOR_TO_CODE = {"aqua": "#00ffff", "ash grey": "#b2beb5", "army green": "#4b5320"}
MAX_COLOR_LENGTH = max(len(name) for name in list(COLOR_TO_CODE.keys()))    #unnecessary for this exercise

for i, color in enumerate(COLOR_TO_CODE):
    print(f"Option {i + 1}: {color}")

color = input("Select color from options: ").lower()
while color != "":
    try:
        print(f"{color} code: {COLOR_TO_CODE[color]}")
    except KeyError:
        print("Invalid Color")
    color = input("Select color from options: ").lower()
