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
def compare_points(ground_truth_path, results_path, threshold):
    ground_truth_points = loadPtsfromJson(ground_truth_path, 'GTPointCoordinates')
    results_points = loadPtsfromJson(results_path, 'DetectedPointCoordinates')

    # Check if both ground truth and results are empty
    if not ground_truth_points:
        return {"distances": [], "detection_successful": True}

    # Test results and ground truth have same size
    if len(ground_truth_points) != len(results_points):
        print(f"Error: Ground truth and results have different number of points")
        return {"distances": [], "detection_successful": False}
    else:
        # Calculate the Euclidean distance between each pair of points
        distances = calculate_euclidean_distance(ground_truth_points, results_points)
        detection_successful = all(distance < threshold for distance in distances)

    # Return the distances and detection success status
    return {"distances": distances.tolist(), "detection_successful": detection_successful}

# Define the main function for Snakemake integration
@click.command()
@click.argument('ground_truth_path', type=click.Path(exists=True), default="data/sample/ground_truth/image_001.json")
@click.argument('results_path', type=click.Path(exists=True), default="results/sample/image_001.json")
@click.argument('threshold', type=float, default=2.0)

def main(ground_truth_path, results_path, threshold):
    # Call the compare_points function and get the results
    results = compare_points(ground_truth_path, results_path, threshold)
    print(f"The distances between ground truth and results points are: {results['distances']}")
    print(f"Detection successful: {results['detection_successful']}")

if __name__ == "__main__":
    main()
