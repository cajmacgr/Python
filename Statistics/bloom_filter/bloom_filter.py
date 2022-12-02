#By Caleb MacGregor
#Some skeleton code provided by Alex Tsun

import numpy as np
import mmh3

class BloomFilter:
    def __init__(self, k:int = 10, m:int=100000):
        self.k = k
        self.m = m
        self.t = np.zeros((k, m), dtype=bool)

    def hash(self, x, i:int) -> int:
        return mmh3.hash(str(x), i) % self.m

    def add(self, x):
        for i in range(self.k):
            self.t[i][self.hash(x, i)] = True

    def contains(self, x) -> bool:

        for i in range(self.k):
            if(self.t[i][self.hash(x, i)] == False):
                return False
        return True

if __name__ == '__main__':

    # Create a new bloom filter structure.
    bf = BloomFilter(k=10, m=8000) # 10 * 8,000 = 80,000 bits = 10 KB

    print("Adding malicious URLS to Bloom Filter")

    # Create our bloom filter of malicious URLs
    mal_urls = np.genfromtxt('data/mal_urls.txt', dtype='str')
    for mal_url in mal_urls:
        bf.add(mal_url)
        #assert bf.contains(mal_url)

    print("(a) Computing False Positive Rate (FPR) on 10000 Unseen URLs")
    # Check contains on 10000 different URLs to see what percentage
    # incorrectly are marked as being contained.
    fpr = 0
    test_urls = np.genfromtxt('data/test_urls.txt', dtype='str')
    for test_url in test_urls:
        if bf.contains(test_url): # Should ideally return False
            fpr += 1
    fpr /= len(test_urls)
    print("The false positive is: {}".format(fpr))
