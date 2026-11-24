from __future__ import annotations
from pydantic import BaseModel
from .rekognition_distribute_dataset import RekognitionDistributeDataset


class RekognitionDistributeDatasetEntriesRequest(BaseModel):
    Datasets: list[RekognitionDistributeDataset]
