#!/usr/bin/env python3

# Author: pachry9

# join_sets will return a set that contains every value from both s1 and s2
def join_sets(s1, s2):
    combined_set = s1.union(s2)
    return combined_set

# match_sets will return a set that contains all values found in both s1 and s2
def match_sets(s1, s2):
    common_set = s1.intersection(s2)
    return common_set

# diff_sets will return a set that contains all different values which are not shared between the sets
def diff_sets(s1, s2):
    unique_set = s1.symmetric_difference(s2)
    return unique_set

# Main code of this script
if __name__ == '__main__':
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))
    print('set1: ', sorted(set1))
    print('set2: ', sorted(set2))
    print('join: ', sorted(join_sets(set1, set2)))
    print('match: ', sorted(match_sets(set1, set2)))
    print('diff: ', sorted(diff_sets(set1, set2)))

