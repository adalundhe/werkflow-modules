from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_dataset import PersonalizeDataset


class PersonalizeDescribeDatasetResponse(BaseModel):
    dataset: PersonalizeDataset | None = None
    ResponseMetadata: dict[str, Any] | None = None
