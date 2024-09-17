import random

# Define the win probabilities for Candidate A in each region
probabilities = [0.87, 0.65, 0.17]

def simulate_election():
    # Simulate voting results for each region
    wins = sum(random.random() < prob for prob in probabilities)
    # Candidate A wins the election if they win in at least 2 of 3 regions
    return wins >= 2

def main():
    num_simulations = 10000
    wins_count = sum(simulate_election() for _ in range(num_simulations))
    
    # Calculate the percentage of elections won by Candidate A
    win_percentage = (wins_count / num_simulations) * 100
    
    # Print the result
    print(f"Candidate A wins {win_percentage:.2f}% of the elections.")

if __name__ == "__main__":
    main()
