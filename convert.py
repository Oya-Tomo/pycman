with open("data", mode="r") as f:
    data = f.read()


rows = data.split("\n")

text = "block_data = [\n"

for row in rows:
    text += "   ["
    columns = row.split(" ")
    for char in columns:
        text += char + ", "
    text += "],\n"

text += "]"

print(text)

with open("black.py", "w") as f:
    f.write(text) 