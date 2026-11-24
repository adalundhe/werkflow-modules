from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_changes import RekognitionDatasetChanges


class RekognitionUpdateDatasetEntriesRequest(BaseModel):
    DatasetArn: StrictStr
    Changes: RekognitionDatasetChanges
