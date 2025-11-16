'''An AnaGram is a word or Phrase formed by Rearranging the letters of a 
 * Different word or phrase  - using all original letters exactly Once.
 * original word or phrase are called 'Subject'
 * any word or phrase that exactly reproduces the letters in another order is an 'anagram'
 * 
 * eg - restful = fluster'''


def is_anagram(s1, s2):
    # If lengths differ, not an anagram
    if len(s1) != len(s2):
        return False

    # Convert to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Count characters manually
    count1 = {}
    count2 = {}

    for ch in s1:
        if ch in count1:
            count1[ch] += 1
        else:
            count1[ch] = 1

    for ch in s2:
        if ch in count2:
            count2[ch] += 1
        else:
            count2[ch] = 1

    # Compare frequency dictionaries
    return count1 == count2


# Testing
print(is_anagram("Adam", "Daneil"))   # False
print(is_anagram("restful", "fluster"))  # True
