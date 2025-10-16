def iou(box1, box2):
    # box format: [x_c, y_c, w, h]
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x1_min, y1_min = x1 - w1/2, y1 - h1/2
    x1_max, y1_max = x1 + w1/2, y1 + h1/2
    x2_min, y2_min = x2 - w2/2, y2 - h2/2
    x2_max, y2_max = x2 + w2/2, y2 + h2/2

    inter_xmin = max(x1_min, x2_min)
    inter_ymin = max(y1_min, y2_min)
    inter_xmax = min(x1_max, x2_max)
    inter_ymax = min(y1_max, y2_max)

    inter_area = max(0, inter_xmax - inter_xmin) * max(0, inter_ymax - inter_ymin)
    area1 = w1 * h1
    area2 = w2 * h2
    union = area1 + area2 - inter_area
    return inter_area / union if union > 0 else 0

def nms(detections, iou_thresh=0.5):
    detections = sorted(detections, key=lambda x: x[1], reverse=True)  # sort by confidence
    keep = []

    while detections:
        best = detections.pop(0)
        keep.append(best)
        detections = [d for d in detections if iou(best[2:], d[2:]) < iou_thresh]
    return keep

def save_detections(final_dets, RESULTS_FILE):
    with open(RESULTS_FILE, "w") as f:
        for det in final_dets:
            cls, conf, x, y, w, h = det
            f.write(f"{cls} {conf:.2f} {x:.1f} {y:.1f} {w:.1f} {h:.1f}\n")

    print(f"✅ Saved merged detections to {RESULTS_FILE}")