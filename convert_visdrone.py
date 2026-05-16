import os

PERSON = [1, 2]
CAR = [4, 5, 6, 9]

base = "/Users/farhanishraq/Documents/Ants AI assessment/datasets/VisDrone_Dataset"

def convert(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if not file.endswith(".txt"):
            continue

        in_path = os.path.join(input_dir, file)
        out_path = os.path.join(output_dir, file)

        new_lines = []

        with open(in_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                cls = int(parts[0])

                if cls in [0, 3, 7, 8]:
                    continue

                if cls in PERSON:
                    new_cls = 0
                elif cls in CAR:
                    new_cls = 1
                else:
                    continue

                new_lines.append(f"{new_cls} {parts[1]} {parts[2]} {parts[3]} {parts[4]}\n")

        with open(out_path, "w") as f:
            f.writelines(new_lines)


# RUN TRAIN + VAL
convert(
    f"{base}/VisDrone2019-DET-train/labels",
    f"{base}/labels/train"
)

convert(
    f"{base}/VisDrone2019-DET-val/labels",
    f"{base}/labels/val"
)

print("DONE")