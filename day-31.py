"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum

number of character insertions, deletions, and substitutions 

required to change one string to the other. For example, 

the edit distance between “kitten” and “sitting” is three: 

substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

"""

def edit_distance(str1, str2, m, n):
    if m==0:
        return n
    if n==0:
        return m
    if (str1[m-1] == str2[n-1]):
        return edit_distance(str1,str2,m-1,n-1)
    return 1 + min(edit_distance(str1, str2, m, n-1),   # insert  
                    edit_distance(str1, str2, m-1, n),  # remove
                    edit_distance(str1, str2, m-1, n-1) # replace
                )
if __name__ == "__main__":
    str1 = ""
    str2 = "monday"

    editDist = edit_distance(str1, str2, len(str1), len(str2))
    print(editDist)