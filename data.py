from pathlib import Path
import shutil

ROOT = Path("./Datasets/CUB_200_2011")

def main():
    images_dir = ROOT / "images"
    train_dir = ROOT / "train"
    test_dir = ROOT / "test"

    train_dir.mkdir(exist_ok=True)
    test_dir.mkdir(exist_ok=True)

    split = {}
    with open(ROOT / "train_test_split.txt") as f:
        for line in f:
            idx, is_train = line.strip().split()
            split[int(idx)] = is_train == "1"

    with open(ROOT / "images.txt") as f:
        for line in f:
            idx, rel_path = line.strip().split()
            idx = int(idx)

            src = images_dir / rel_path
            if not src.exists():
                print(f"Missing: {src}")
                continue

            target_root = train_dir if split[idx] else test_dir
            class_dir = target_root / src.parent.name
            class_dir.mkdir(parents=True, exist_ok=True)

            dst = class_dir / src.name
            shutil.copy2(src, dst)

    print("train / test folders created successfully")

if __name__ == "__main__":
    main()
