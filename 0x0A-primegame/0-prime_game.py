def sieve_of_eratosthenes(max_n):
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        is_prime_removed = [False] * (n + 1)
        prime_count = 0

        for prime in primes:
            if prime > n:
                break
            if not is_prime_removed[prime]:
                prime_count += 1
                for multiple in range(prime, n + 1, prime):
                    is_prime_removed[multiple] = True

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
