import numpy as np

def loadPtsfromJson(path, description):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            points = data.get(description, [])
            return points
    except FileNotFoundError:
        print(f"Error: Ground truth file not found at {path}")
        return 
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON data in ground truth file at {path}")
        return 
    
def compute_metrics(detected_points, ground_truth_points, threshold):
    """
    Compute metrics for detected points.
    
    Parameters:
    detected_points (list of np.array): List of detected points for each image.
    ground_truth_points (list of np.array): List of ground truth points for each image.
    threshold (float): Threshold for considering a point as correctly detected.
    
    Returns:
    dict: Dictionary containing mean, std, and percentage of correctly detected points.
    """
    correctly_detected = []
    for detected, ground_truth in zip(detected_points, ground_truth_points):
        distances = np.linalg.norm(detected - ground_truth, axis=1)
        correct = distances <= threshold
        correctly_detected.append(correct)
    
    correctly_detected_points = [detected[correct] for detected, correct in zip(detected_points, correctly_detected)]
    correctly_detected_points = np.concatenate(correctly_detected_points, axis=0)
    
    mean = np.mean(correctly_detected_points, axis=0)
    std = np.std(correctly_detected_points, axis=0)
    
    percentage_correct = np.mean([np.any(correct) for correct in correctly_detected]) * 100
    
    return {
        'mean': mean,
        'std': std,
        'percentage_correct': percentage_correct
    }

# Example usage
detected_points = [np.array([[10, 20], [30, 40]]), np.array([[15, 25], [35, 45]])]
ground_truth_points = [np.array([[12, 22], [32, 42]]), np.array([[14, 24], [34, 44]])]
threshold = 5.0


@click.command()
@click.argument('ground_truth_path', type=click.Path(exists=True), default="data/sample/ground_truth/image_006.json")
@click.argument('results_path', type=click.Path(exists=True), default="results/sample/image_006.json")
def main(ground_truth_path, results_path):
    threshold = 5.0
    # Call the compare_points function and print the distances
    metrics = compute_metrics(detected_points, ground_truth_points, threshold)
    print(f"Computed Metrics: {metrics}")

if __name__ == "__main__":
    main()
