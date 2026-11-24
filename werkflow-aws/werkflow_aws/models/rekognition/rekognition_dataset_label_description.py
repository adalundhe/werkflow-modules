from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_label_stats import RekognitionDatasetLabelStats


class RekognitionDatasetLabelDescription(BaseModel):
    LabelName: StrictStr | None = None
    LabelStats: RekognitionDatasetLabelStats | None = None
