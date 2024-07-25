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

    # Example results
    print (centroids)

if __name__ == "__main__":
    main()





