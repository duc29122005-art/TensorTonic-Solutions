def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    if not boxes:
        return []
    def iou(box1, box2):
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        xx = max(0, x2 - x1)
        yy = max(0, y2 - y1)

        area = xx * yy

        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

        hehe = area1 + area2 - area
        if(hehe == 0):
            return 0.0

        return area / hehe

    order = sorted(range(len(boxes)), key=lambda i : scores[i], reverse = True)
    kept=[]

    while order: 
        current = order.pop(0)
        kept.append(current)

        remaining = []
        for idx in order:
            if iou(boxes[current], boxes[idx]) < iou_threshold:
                remaining.append(idx)
        order = remaining
    return kept
    # Write code here
    pass