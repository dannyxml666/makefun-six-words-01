import os

def main():
    story = "She came home; locks were changed."
    
    # Harden validation
    words = story.split()
    assert len(words) == 6, f"Expected 6 words, got {len(words)}"
    assert 1 <= len(story) <= 60, f"Length {len(story)} out of bounds"
    
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story)

if __name__ == "__main__":
    main()
