
## MODEL ##
IMAGE_SIZE = 200
BATCH_SIZE = 1
EVAL_STEPS = 1
CHECKPOINT_DIR = "./data/model"
CHECKPOINT_NAME = "model.pth.tar"
LOG_DIR = "./data/logs"

## DATASET ##
DATA_PATH = "./data/sets/{name}"
IMAGES_PATH = "images/{id_}.jpg"
ANNOTATIONS_PATH = "annotations/{id_}.txt"
EVALSET_PCT = .1
CROP_TO_SIZE = (1024, 1020)  # H, W