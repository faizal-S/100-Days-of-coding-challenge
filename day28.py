import random

def simulate_coin_flips():
    seen_heads = False
    seen_tails = False
    flips_count = 0
    
    while not (seen_heads and seen_tails):
        flip = random.choice(['H', 'T'])
        if flip == 'H':
            seen_heads = True
        if flip == 'T':
            seen_tails = True
        flips_count += 1
    
    return flips_count

def main():
    num_trials = 10000
    total_flips = 0
    
    for _ in range(num_trials):
        total_flips += simulate_coin_flips()
    
    average_flips = total_flips / num_trials
    print(f"Average number of flips per trial: {average_flips:.2f}")

if __name__ == "__main__":
    main()
