from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_metadata import RekognitionDatasetMetadata


class RekognitionProjectDescription(BaseModel):
    ProjectArn: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Datasets: list[RekognitionDatasetMetadata] | None = None
    Feature: StrictStr | None = None
    AutoUpdate: StrictStr | None = None
