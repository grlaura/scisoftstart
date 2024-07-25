def detectBlobsinImg(image, draw=False):
    import cv2
    import numpy as np

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create an MSER detector
    mser = cv2.MSER_create()

    # Detect MSER regions
    msers, bboxes = mser.detectRegions(gray)
    centroids = np.zeros((len(msers), 2), dtype=float)

    # Iterate over each MSER region to calculate its centroid
    for i, region in enumerate(msers):
        # Calculate moments for the current region
        M = cv2.moments(region)
        
        # Check if the area (m00) is not zero to avoid division by zero
        if M['m00'] != 0:
            cx = M['m10'] / M['m00']
            cy = M['m01'] / M['m00']
            centroids[i] = [cx, cy]
        else:
            # Handle the case when the area is zero, which means no centroid can be found
            centroids[i] = [np.nan, np.nan]  # Or any other appropriate handling  

    if draw:
            # Draw bounding boxes on the image
        for i, box in bboxes:
            x, y, w, h = box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        # Draw the result
        cv2.imshow('Image with Bounding Boxes', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return centroids


