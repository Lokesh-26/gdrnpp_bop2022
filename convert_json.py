import os
import json


def transform_json(original_json):
    transformed_data = {}
    # loop through all indices in the original json
    # loop through only 2 indices in the original json
    for image_data in original_json:
        scene_id = image_data["scene_id"]
        image_id = image_data["image_id"]
        key = f"{scene_id}/{image_id}"
        transformed_data[key] = []

        transformed_item = {
            "bbox_est": image_data["bbox"],
            "obj_id": image_data["category_id"],
            "score": image_data.get("score", 1.0),  # Assuming a default score of 1.0 if not present
            "time": image_data.get("time", 0.0),  # Assuming a default time of 0.0 if not present
        }
        transformed_data[key].append(transformed_item)

    return transformed_data


# Example usage
# read json file
with open(
        "/media/gouda/3C448DDD448D99F2/segmentation/gdrnpp_bop2022/datasets/BOP_DATASETS/br6d/test/test_bboxes/br6d_test_coco_format.json",
        "r") as f:
    original_json_data = json.load(f)

transformed_data = transform_json(original_json_data)
# write json file
with open("br6d_test_coco_format.json", "w") as f:
    json.dump(transformed_data, f)