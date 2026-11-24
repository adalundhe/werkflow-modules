from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_dataset_label_description import RekognitionDatasetLabelDescription


class RekognitionListDatasetLabelsResponse(BaseModel):
    DatasetLabelDescriptions: list[RekognitionDatasetLabelDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
