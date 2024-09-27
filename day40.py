def toggle_cats_with_hats(num_cats):
    # Initialize a list of cats, all starting with no hats (False)
    cats = [False] * num_cats
    
    # Perform the rounds
    for round in range(1, num_cats + 1):
        for cat in range(round - 1, num_cats, round):
            cats[cat] = not cats[cat]  # Toggle the hat status
    
    # Collect the indices of cats that have hats (True)
    cats_with_hats = [i + 1 for i, has_hat in enumerate(cats) if has_hat]
    
    return cats_with_hats

# Number of cats
num_cats = 100
result = toggle_cats_with_hats(num_cats)

print("Cats with hats:", result)
