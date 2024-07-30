import json
import numpy as np
import click

# Define the function to calculate Euclidean distance
def calculate_euclidean_distance(gt_points, result_points):
    return np.linalg.norm(np.array(gt_points) - np.array(result_points), axis=1)

def loadPtsfromJson(path, description):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            points = data.get(description, [])
            return points
    except FileNotFoundError:
        print(f"Error: Ground truth file not found at {path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON data in ground truth file at {path}")
        return []

# Define the function to compare points
def compare_points(ground_truth_path, results_path):
    ground_truth_points = loadPtsfromJson(ground_truth_path, 'GTPointCoordinates')
    results_points = loadPtsfromJson(results_path, 'DetectedPointCoordinates')
    # Calculate the Euclidean distance between each pair of points
    distances = calculate_euclidean_distance(ground_truth_points, results_points)

    # Return the distances
    return distances

# Define the main function for Snakemake integration
@click.command()
@click.argument('ground_truth_path', type=click.Path(exists=True), default="data/sample/ground_truth/image_006.json")
@click.argument('results_path', type=click.Path(exists=True), default="results/sample/image_006.json")
def main(ground_truth_path, results_path):
    # Call the compare_points function and print the distances
    distances = compare_points(ground_truth_path, results_path)
    print(f"The distances between ground truth and results points are: {distances}")

if __name__ == "__main__":
    main()
