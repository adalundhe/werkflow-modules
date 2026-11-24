from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_stats import RekognitionDatasetStats


class RekognitionDatasetDescription(BaseModel):
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    StatusMessageCode: StrictStr | None = None
    DatasetStats: RekognitionDatasetStats | None = None
