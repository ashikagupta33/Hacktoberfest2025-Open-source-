# code_poem.py
# Usage: python code_poem.py script.py
import sys, re, random

def extract_words(code):
    comments = re.findall(r'#.*', code)
    names = re.findall(r'\b([A-Za-z_][A-Za-z0-9_]{2,})\b', code)
    strings = re.findall(r'(["\']{1,3})(?:(?!\1).)*\1', code, flags=re.S)
    words = []
    for c in comments:
        words += re.findall(r"[A-Za-z']{2,}", c)
    for s in strings:
        words += re.findall(r"[A-Za-z']{2,}", s)
    for n in names:
        if len(n)>2:
            split = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', n)
            words += [w.lower() for w in split if len(w)>1]
    return [w for w in words if len(w)>1]

def make_poem(words, lines=6):
    random.shuffle(words)
    poem = []
    i = 0
    for _ in range(lines):
        length = random.randint(3,7)
        line_words = []
        for _ in range(length):
            if i >= len(words):
                words = words[::-1]
                i = 0
            word = words[i]
            i += 1
            line_words.append(word)
        line = " ".join(line_words).capitalize()
        poem.append(line)
    return "\n".join(poem)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python code_poem.py path/to/code.py")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    words = extract_words(code)
    if not words:
        print("No words found to craft a poem.")
    else:
        print("\n✨ Code Poem ✨\n")
        print(make_poem(words, lines=7))
