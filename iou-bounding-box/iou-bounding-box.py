def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here

    x1 = max(box_a[0], box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])

    w = max(0, x2 - x1)
    h = max(0, y2 - y1)

    area1 = max(0, (box_a[2] - box_a[0])) * max(0, (box_a[3] - box_a[1]))
    area2 = max(0, (box_b[2] - box_b[0])) * max(0, (box_b[3] - box_b[1]))

    union = area1 + area2 - w * h

    if union == 0:
        return 0.0
    return w * h / union
    pass