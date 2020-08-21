# -*- coding: utf-8 -*-
IMAGE_BLOCK_TYPE = 1
TEXT_BLOCK_TYPE = 0


def split_blocks(raw_dict: dict):
    new_dict = {"height": raw_dict["height"], "width": raw_dict["width"], "blocks": []}
    for block in raw_dict["blocks"]:
        if block["type"] == IMAGE_BLOCK_TYPE:
            new_dict["blocks"].append(block)
        elif block["type"] == TEXT_BLOCK_TYPE:
            for line in block["lines"]:
                print(line["bbox"][0], block["bbox"][0])
                print(line["bbox"][2], block["bbox"][2])
                new_line = {"type": TEXT_BLOCK_TYPE, "lines": [line], "bbox": (
                    min(line["bbox"][0], block["bbox"][0]), line["bbox"][1], max(line["bbox"][2], block["bbox"][2]), line["bbox"][3])}
                new_dict["blocks"].append(new_line)
                # new_dict["blocks"].append({
                #     "type": TEXT_BLOCK_TYPE,
                #     "lines": [line],
                #     "bbox": line["bbox"]
                # })
    return new_dict
