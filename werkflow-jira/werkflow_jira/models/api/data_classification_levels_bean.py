from __future__ import annotations
from pydantic import BaseModel
from .data_classification_tag_bean import DataClassificationTagBean


class DataClassificationLevelsBean(BaseModel):
    classifications: list[DataClassificationTagBean] | None = None
