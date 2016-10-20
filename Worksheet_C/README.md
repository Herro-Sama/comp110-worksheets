# Worksheet C

(a) This algorithm scans through a single list and compares every single item to check for duplicate items.
(b) The reason that this algorithm is quadratic, is because everytime you add a new item the algorithm has to run the new addition against every possible result in the list.
(c) The algorithm is still correct, as it runs previous items in the list against the new item meaning that once completed it will have compared all items but doesn't make duplicate comparisons.
(d) The algorithm is half as fast because it only has to make half the comparisons after removing the duplicate comparisons
(e) Yes it is still quadratic as it does n “things” and each “thing” is O(n), then the overall algorithm is O(n**2)
(f) http://stackoverflow.com/questions/23809785/python-sorting-complexity-on-sorted-list - "Best case scenario: O(n), average and worst case O(nlogn). – Martijn Pieters"
(g) I think the answer would be O(nlogn) as that is the worst case scenario of the sorting function.
(h) If the list is large, it would be faster to run the intial method as although it is slower to complete. It is faster than having to sort a large disorganised list.
(i) A designer may decide to use the slower method for two reasons, one: they are unsure of how to use a faster method and it was easier to do a linear search. Two: They have a long unsorted list and don't want to spend a large amount of time sorting the list so they can implement the second method.