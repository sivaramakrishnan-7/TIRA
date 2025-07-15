import time

def append_or_pop(n):
    result = [] 
    
    start_add = time.time()
    for i in range(1, n+1):
        result.append(i)
    end_add = time.time()
    time_add =  end_add - start_add

    print(f"Time taken for {n} additions: {time_add:.6f} seconds")
    print(f"List length after additions: {len(result)}")

    start_del = time.time()
    for _ in range(n):
        result.pop()
    end_del = time.time()
    time_del =  end_del - start_del

    print(f"Time taken for {n} deletions: {time_del:.6f} seconds")
    print(f"List length after deletions: {len(result)}")
    print("\n--- Test Complete ---")

if __name__ == "__main__":
    n = 10**5
    append_or_pop(n)

