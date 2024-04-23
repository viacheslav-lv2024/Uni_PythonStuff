import argparse
import math
from multiprocessing import Pool

def sum_of_fractions(args):
    start, end = args
    total_sum = sum(1 / k for k in range(start, end + 1))
    return total_sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Approximate Euler-Mascheroni constant using multiprocessing.')
    parser.add_argument('-n', '--num-terms', type=int, default=10000, help='Number of terms in the sum')
    parser.add_argument('-p', '--processes', type=int, default=1, help='Number of processes')
    args = parser.parse_args()

    terms_per_process = args.num_terms // args.processes
    pool_args = [(i * terms_per_process + 1, (i + 1) * terms_per_process) for i in range(args.processes)]

    with Pool(args.processes) as pool:
        results = pool.map(sum_of_fractions, pool_args)

    total_sum = sum(results)
    gamma_approximation = total_sum - math.log(args.num_terms)

    print(f'Euler-Mascheroni constant approximation ({args.num_terms} terms): {gamma_approximation:.9f}')
