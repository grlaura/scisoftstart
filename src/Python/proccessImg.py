import json
import cv2
import os
from loadAndShowImg import loadAndShowImg
import click

@click.command()
@click.argument("path", type=click.Path(exists=True))
def main(path):
    # Load and show the image
    #loadAndShowImg(path)

    # Load the image
    image = cv2.imread(path)

    # Example processing results
    numbers = [1, 2, 3, 4, 5]

    print (numbers)

if __name__ == "__main__":
    main()





