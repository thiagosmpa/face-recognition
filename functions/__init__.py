import torch
import torch.nn as nn
import cv2
from PIL import Image
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

import random

def set_seed(seed=42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)

set_seed()

from .pth_processing import pth_processing
from .FaceTransformer import FaceTransformer
from .detect_face import detect_face
from .compare_embeddings import compare_embeddings
from .extract_features import extract_features
from .db import add_face, get_embeddings, update_embeddings

__all__ = [
    "pth_processing",
    "FaceTransformer",
    "detect_face",
    "compare_embeddings",
    "extract_features",
    "add_face",
    "get_embeddings",
    "update_embeddings"
]