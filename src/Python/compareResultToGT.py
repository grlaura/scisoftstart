import json
import numpy as np
import click

# Define the function to calculate Euclidean distance
def calculate_euclidean_distance(gt_points, result_points):
    return np.linalg.norm(np.array(gt_points) - np.array(result_points), axis=1)

# Define the function to compare points
def compare_points(ground_truth_path, results_path):
    # Load ground truth data
    with open(ground_truth_path, 'r') as gt_file:
        ground_truth_data = json.load(gt_file)
        ground_truth_points = ground_truth_data['GTPointCoordinates']

    # Load results data
    with open(results_path, 'r') as results_file:
        results_points = json.load(results_file)

    # Calculate the Euclidean distance between each pair of points
    distances = calculate_euclidean_distance(ground_truth_points, results_points)

    # Return the distances
    return distances

# Define the main function for Snakemake integration
@click.command()
@click.argument('ground_truth_path', type=click.Path(exists=True), default="data/full_01/ground_truth/image_001.json")
@click.argument('results_path', type=click.Path(exists=True), default="results/full_01/image_001.json")
def main(ground_truth_path, results_path):
    # Call the compare_points function and print the distances
    distances = compare_points(ground_truth_path, results_path)
    print(f"The distances between ground truth and results points are: {distances}")

if __name__ == "__main__":
    main()
