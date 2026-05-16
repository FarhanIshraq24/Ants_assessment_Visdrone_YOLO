import os

class_map = {
    1: 0,  # pedestrian → person
    2: 0,  # people → person
    4: 1,  # car
    5: 1,  # van
    6: 1,  # truck
    9: 1   # bus
}

input_dir = "datasets/VisDrone_Dataset/VisDrone2019-DET-train/labels"
output_dir = "datasets/yolo/labels/train"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if not file.endswith(".txt"):
        continue

    with open(os.path.join(input_dir, file), "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        parts = line.strip().split()

        cls = int(parts[0])

        if cls not in class_map:
            continue

        x, y, w, h = parts[1:5]

        new_cls = class_map[cls]

        new_lines.append(f"{new_cls} {x} {y} {w} {h}")

    with open(os.path.join(output_dir, file), "w") as f:
        f.write("\n".join(new_lines))