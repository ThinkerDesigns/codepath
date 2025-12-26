def min_distance(words, word1, word2):
    idx = 0
    for i in range(len(words)):
        if words[i] == word1:
           idx = i
    for i in range(len(words)):
        if words[i] == word2:
            return abs(i - idx)

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)


'''
   pos1 = -1
   pos2 = -1
   min_dist = float('inf')
   for index, word in enumerate(words):
      if word == word1:
        pos1 = index
      if word == word2:
         pos2 = index
   min_dist = abs(pos1 - pos2)
   return min_dist
   '''