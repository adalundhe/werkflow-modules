from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rekognition_dataset_description import RekognitionDatasetDescription


class RekognitionDescribeDatasetResponse(BaseModel):
    DatasetDescription: RekognitionDatasetDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
