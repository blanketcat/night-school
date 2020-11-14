#!/usr/bin/env python3

"""
	From Wikipedia: https://en.wikipedia.org/wiki/Monte_Carlo_method
	Monte Carlo methods vary, but tend to follow a particular pattern:

    1) Define a domain of possible inputs
    2) Generate inputs randomly from a probability distribution over the domain
    3) Perform a deterministic computation on the inputs
    4) Aggregate the results
"""


def monte_carlo(domain_min, domain_max, rand_function, n_rand_samples, aggregation_function):
	sample_space = []
	for i in range(n_rand_samples):
		sample_space.append(rand_function(domain_min, domain_max))
	return aggregation_function(sample_space)


def main():
	pass


if __name__ == '__main__':
	main()
