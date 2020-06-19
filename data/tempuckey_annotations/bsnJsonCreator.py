import pandas as pd
import argparse
import os.path as osp
import json
from tqdm import tqdm


def parseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label_file", type=str,
                        default="/usr/local/data02/zahra/datasets/Tempuckey/labels/tempuckey_ground_truth_annotations.json", help="label file")
    parser.add_argument("--video_file", type=str,
                        default="/usr/local/data02/pengnanf/BSN-boundary-sensitive-network.pytorch/data/tempuckey_annotations/tempuckey_video_info_split.csv", help="video file")
    parser.add_argument("--video_dir", type=str,
                        default="/usr/local/data02/zahra/datasets/Tempuckey/all_videos_UNLABELED", help="raw video directory")
    parser.add_argument("--json_name", type=str,
                        default="tempuckey_label.json", help="json file name")
    parser.add_argument("--output_dir", type=str,
                        default=".", help="place to store output")
    return parser.parse_args()


def main(config):
    if not osp.isfile(config.label_file):
        raise RuntimeError(
            "Cannot find the label file: {}".format(config.label_file))

    if not osp.isfile(config.video_file):
        raise RuntimeError(
            "Cannot find the video info file: {}".format(config.video_file))

    json_file = dict()

    with open(config.label_file, "r") as f:
        label_file = json.load(f)["results"]

    video_info = pd.read_csv(config.video_file)

    for line in tqdm(video_info.itertuples()):
        values = dict()

        values["duration_frame"] = line.numFrame
        values["duration_second"] = line.seconds

        if line.video in label_file:
            label_infos = label_file[line.video]

            anno = list()
            for label in label_infos:
                anno.append(
                    {"segment": label["segment"], "label": "faceoff"})

            values["annotations"] = anno
            json_file[line.video] = values

    with open(osp.join(config.output_dir, config.json_name), "w") as f:
        json.dump(json_file, f)


if __name__ == '__main__':
    main(parseInput())
