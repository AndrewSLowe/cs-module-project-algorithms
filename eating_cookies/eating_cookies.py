# First pass!!
def eating_cookies(n):   # 3**n operations
    # base case: when there are no more cookies
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # This represents our recursive case where there are still cookies to be eaten
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# cachine/memoization: let's save our work so we don't have
# to recompute it again

# Need some sort of data structure where we'll save the data
# arrays and dictionaries
# If we check our cache and see that the answer we're looking for is
# already in there, just return that answer
# what if the cache doesn't have what we're looking for? Or how do we
# get answers in there?
# There's going to be a first time for caluclating an answer, and we're
# going to do it the same way we're currently doing it. 

def eating_cookies(n, cache=None):
    print(n)
    # base case: when there are no more cookies
    if n == 0:
        return 1
    # check for negative n values
    elif n < 0:
        return 0
    # init our cache if we don't have it yet
    # add a case to have us check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
        # we can go ahead and save our answer to the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    # This represents our recursive case where there are still cookies to be eaten
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
