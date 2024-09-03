def main():
    path = 'books/frankenstein.txt'
    print(f"--- Begin report of {path} ---")
    text = get_txt(path)
    numWords = count_words(text)
    print(f"{numWords} words found in the document \n")
    
    SortedLetteCount = d_sort(count_letters(text))
    
    for (idx, cnt) in enumerate(SortedLetteCount):
        alpha, count = cnt[0], cnt[1]
        print(f"The {alpha} character was found {count} times")

    print("--- End Report ---")

def get_txt(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())


def count_letters(string):
    string = string.lower()
    freq = {}
    for c in set(string):
        freq[c] = string.count(c)
    return freq

def d_sort(d):
    d = {key: value for key, value in d.items() if key.isalpha()}
    
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

main()