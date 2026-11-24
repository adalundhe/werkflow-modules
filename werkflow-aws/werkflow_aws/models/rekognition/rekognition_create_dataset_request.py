from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_source import RekognitionDatasetSource


class RekognitionCreateDatasetRequest(BaseModel):
    DatasetType: Literal['TRAIN', 'TEST']
    ProjectArn: StrictStr
    DatasetSource: RekognitionDatasetSource | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
