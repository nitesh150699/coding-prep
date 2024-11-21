'''
The Knuth-Morris-Pratt (KMP) algorithm is a string-matching algorithm that searches for occurrences of a "pattern" string within a "text"
 string in an efficient manner. It does this by preprocessing the pattern to create a longest prefix suffix (LPS) array,
   which is used to skip unnecessary comparisons in the text.

'''

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    result = [] 
    text_length = len(text)
    pattern_length = len(pattern)

    i = 0  
    j = 0 

    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_length:
            result.append(i - j)  
            j = lps[j - 1]

        elif i < text_length and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  
            else:
                i += 1  

    return result

def compute_lps(pattern):
    length = 0  
    lps = [0] * len(pattern)  
    i = 1  

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  
            else:
                lps[i] = 0
                i += 1

    return lps

if __name__ == "__main__":
    text = "ababcababcabc"
    pattern = "abc"
    matches = kmp_search(text, pattern)
    print("Pattern found at indices:", matches)  # Output: [2, 7, 12]
