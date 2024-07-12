def loadAndShowImg(image_path):
    import os
    import cv2

    # Load the image
    image = cv2.imread(image_path)

    # Check if the file exists
    if os.path.isfile(image_path):
        # Try to open the image
        image = cv2.imread(image_path)
        if image is not None:
            print('Image loaded successfully')
            cv2.imshow('Image', image)
            # Wait for a key press to close the window
            cv2.waitKey(5000)
            cv2.destroyAllWindows()
        else:
            print('Image is not loaded, the file may be corrupted or in an unsupported format')
    else:
        print('File does not exist at the specified path')