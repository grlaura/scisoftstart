import json
import cv2
import numpy as np
import os
from loadAndShowImg import loadAndShowImg
from detectBlobsinImg import detectBlobsinImg
import click

@click.command()
@click.argument("path", type=click.Path(exists=True), default="data/full_01/images/image_001.png")
def main(path):
    # Load and show the image
    #loadAndShowImg(path)

    # Load the image
    image = cv2.imread(path)

    #loadAndShowImg(path)

    # Processing
    centroids = detectBlobsinImg(image, False)

        # Convert centroids to the correct format if necessary
    # Assuming 'centroids' is a NumPy array, convert it to a list of lists
    centroids_list = centroids.tolist() if isinstance(centroids, np.ndarray) else centroids

    # Create a dictionary with the desired key and the list of centroids
    output_data = {"DetectedPointCoordinates": centroids_list}

    # Print the dictionary as a JSON-formatted string
    print(json.dumps(output_data))

if __name__ == "__main__":
    main()





