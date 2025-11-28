import time
 
def brute_force_factor(n):
    """Try every number from 2 up to sqrt(n) to factor n.
       Educational-only: works only for small numbers."""
    
    start_time = time.time()   # Start timer
    
    limit = int(n**0.5) + 1
 
    for x in range(2, limit):
        if n % x == 0:
            p = x
            q = n // x
            end_time = time.time()    # End timer
            elapsed = end_time - start_time
            return p, q, elapsed
 
    end_time = time.time()
    elapsed = end_time - start_time
    return None, None, elapsed

set_of_primes = {
    5:[99991, 10007],
    8:[10000019, 10000103],
    9:[265371653,2462372461],
    10:[7971295931 , 8018018081]
}

def example(digits=5):
    p, q = set_of_primes[digits]
    n = p * q
    p_found, q_found, elapsed = brute_force_factor(n)
    print(f"Factors of {n} are {p_found} and {q_found}. Found in {elapsed:.6f} seconds.")


menu_text = "Enter \n5 for very small example\n8 for small example\n9 for normal example\n10 for large example\nq to quit: "
choice = input(menu_text)
while (choice!="q"):
    example(int(choice))
    choice = input(menu_text)
