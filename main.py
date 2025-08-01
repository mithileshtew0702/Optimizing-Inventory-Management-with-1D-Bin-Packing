import json
import time
import random
from datetime import datetime

# Initialize random seed for reproducibility
random.seed(0)

def read_bin_packing_instances(json_file_path):
    """Read bin packing instances from a JSON file"""
    with open(json_file_path, 'r') as f:
        return json.load(f)

#Greedy Heuristic Algorithms
#######################################################################
def first_fit(item_list, bin_capacity):
    """
    First-fit bin packing algorithm
    Places each item into the first bin that has enough space
    """
    bins = []
    remaining_space = []
    
    for current_item in item_list:
        item_placed = False
        
        # Try to place item in existing bins
        for idx in range(len(bins)):
            if remaining_space[idx] >= current_item:
                bins[idx].append(current_item)
                remaining_space[idx] -= current_item
                item_placed = True
                break
        
        # If item couldn't be placed, create new bin
        if not item_placed:
            bins.append([current_item])
            remaining_space.append(bin_capacity - current_item)
    
    return bins

def first_fit_decreasing(item_list, bin_capacity):
    """
    First-fit decreasing variant
    Sorts items in descending order before applying first-fit
    """
    sorted_items = sorted(item_list, reverse=True)
    return first_fit(sorted_items, bin_capacity)

def best_fit(item_list, bin_capacity):
    """
    Best-fit bin packing algorithm
    Places each item into the bin that will have the least remaining space after placement
    """
    bins = []
    remaining_space = []
    
    for current_item in item_list:
        best_index = -1
        smallest_remaining = bin_capacity + 1 # Initialize with impossible value
        
         # Find the best bin for current item
        for idx in range(len(bins)):
            space_after_placement = remaining_space[idx] - current_item
            if 0 <= space_after_placement < smallest_remaining:
                smallest_remaining = space_after_placement
                best_index = idx
        
        # Place item in best bin or create new bin
        if best_index >= 0:
            bins[best_index].append(current_item)
            remaining_space[best_index] = smallest_remaining
        else:
            bins.append([current_item])
            remaining_space.append(bin_capacity - current_item)
    
    return bins

def best_fit_decreasing(item_list, bin_capacity):
    """
    Best-fit decreasing variant
    Sorts items in descending order before applying best-fit
    """
    sorted_items = sorted(item_list, reverse=True)
    return best_fit(sorted_items, bin_capacity)
#######################################################################

#Genetic Algorithm
#######################################################################
def select_parent(population, tournament_size):
    """
    Tournament selection for genetic algorithm
    Selects the best individual from a random subset of the population
    """
    return min(random.sample(population, tournament_size), 
              key=lambda individual: individual['fitness'])

def crossover(parent1, parent2):
    """
    Order crossover for genetic algorithm
    Creates offspring by preserving a subsequence from one parent and filling the rest from the other
    """
    chromosome_length = len(parent1)
    point1, point2 = sorted(random.sample(range(chromosome_length), 2))
    
    offspring = [None] * chromosome_length
    offspring[point1:point2] = parent1[point1:point2]
    
    # Fill remaining positions with genes from parent2 in order and skipping duplicates
    remaining_genes = [gene for gene in parent2 if gene not in offspring]
    insert_position = 0
    
    for i in range(chromosome_length):
        if offspring[i] is None:
            offspring[i] = remaining_genes[insert_position]
            insert_position += 1
    
    return offspring

def genetic_algorithm_packing(items, capacity, max_time):
    """
    Genetic algorithm for bin packing problem
    Uses permutation-based encoding and tournament selection
    """
    item_count = len(items)
    # Sort indices by item size for initial solutions
    sorted_indices = sorted(range(item_count), 
                         key=lambda i: items[i], reverse=True)
    
    # Algorithm parameters
    population_size = 30
    tournament_size = 5
    crossover_prob = 0.85
    mutation_prob = 0.2
    
    # Initialize population with heuristic solutions
    population = []
    initial_permutations = [
        sorted_indices, # Sorted by size
        list(range(item_count)), # Original order
        random.sample(range(item_count), item_count) # Random order
    ]
    
    # Create initial population with some heuristic solutions
    for permutation in initial_permutations:
        solution = best_fit([items[i] for i in permutation], capacity)
        population.append({
            'perm': permutation,
            'fitness': len(solution) # Fitness = number of bins used
        })
    
    # Complete population with random solutions
    while len(population) < population_size:
        random_perm = random.sample(range(item_count), item_count)
        solution = best_fit([items[i] for i in random_perm], capacity)
        population.append({
            'perm': random_perm,
            'fitness': len(solution)
        })
    
    # Track best solution found
    best_solution = min(population, key=lambda x: x['fitness'])
    algorithm_start = time.time()
    last_improvement = algorithm_start
    stagnation_limit = max_time * 0.2
    
    # Main Gentic Algorithm loop
    while time.time() - algorithm_start < max_time:
        new_population = [best_solution] # Keep best solution
        
        while len(new_population) < population_size:
            # Selection
            parent1 = select_parent(population, tournament_size)
            parent2 = select_parent(population, tournament_size)
            
            # Crossover
            if random.random() < crossover_prob:
                child = crossover(parent1['perm'], parent2['perm'])
            else:
                child = parent1['perm'].copy() # Clone parent if no crossover
            
            # Mutation
            if random.random() < mutation_prob:
                idx1, idx2 = random.sample(range(item_count), 2)
                child[idx1], child[idx2] = child[idx2], child[idx1]
            
            # Evaluation
            packing = best_fit([items[i] for i in child], capacity)
            fitness_value = len(packing)
            new_population.append({
                'perm': child,
                'fitness': fitness_value
            })
            
            # Update best solution if improved
            if fitness_value < best_solution['fitness']:
                best_solution = {
                    'perm': child,
                    'fitness': fitness_value
                }
                last_improvement = time.time()
        
        population = new_population
        
         # Early termination if no improvement for stagnation period
        if time.time() - last_improvement > stagnation_limit:
            break
    
    # Return best solution found
    final_packing = best_fit([items[i] for i in best_solution['perm']], capacity)
    return final_packing, best_solution['fitness']
#######################################################################

# Main Content
#######################################################################
if __name__ == "__main__":
    INPUT_FILE = 'CW_ins.json'
    OUTPUT_FILE = 'solution.json'
    TIME_LIMIT = 300.0
    
    # Read problem instances
    problem_instances = read_bin_packing_instances(INPUT_FILE)
    execution_start = time.time()
    
    # Prepare results structure
    results = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'time': 0,
        'res': []
    }
    total_bin = 0
    
    # Allocate time equally among problem instances
    time_per_problem = TIME_LIMIT / len(problem_instances)
    
    # Process each problem instance
    for instance in problem_instances:
        instance_name = instance['name']
        item_sizes = instance['items']
        bin_size = instance['capacity']
        
        # Execute greedy approaches
        ff_result = first_fit(item_sizes, bin_size)
        ffd_result = first_fit_decreasing(item_sizes, bin_size)
        bf_result = best_fit(item_sizes, bin_size)
        bfd_result = best_fit_decreasing(item_sizes, bin_size)
        
        # Determine best greedy solution
        greedy_results = [ff_result, ffd_result, bf_result, bfd_result]
        optimal_greedy = min(greedy_results, key=lambda x: len(x))
        greedy_bin_count = len(optimal_greedy)
        
        print(f"\nProcessing: {instance_name}")
        print(f"  Greedy solution Bins: {greedy_bin_count}")
        
        # Execute Genetic Algorithm with time limit
        print(f"  Executing GA (≈{time_per_problem:.1f}s)...", end='', flush=True)
        ga_start_time = time.time()
        ga_packing, ga_bin_count = genetic_algorithm_packing(
            item_sizes, bin_size, time_per_problem)
        ga_execution_time = time.time() - ga_start_time
        print(f"  → GA Bins: {ga_bin_count} (t={ga_execution_time:.3f}s)")
        
        # Select best solution between greedy and Genetic Algorithm
        if ga_bin_count < greedy_bin_count:
            chosen_solution = ga_packing
            bin_count = ga_bin_count
        else:
            chosen_solution = optimal_greedy
            bin_count = greedy_bin_count
        
        # Record results
        total_bin += bin_count
        results['res'].append({
            'name': instance_name,
            'capacity': bin_size,
            'solution': chosen_solution
        })
#######################################################################

    # Finalize and save results
    results['time'] = time.time() - execution_start
    
    with open(OUTPUT_FILE, 'w') as output_file:
        json.dump(results, output_file, indent=4)
    
    # Print summary
    print("\n--- Summary ---")
    print(f"Output saved to {OUTPUT_FILE}")
    print(f"Total Used Bins: {total_bin}")
    print(f"Total Execution Time: {results['time']:.3f}s")
