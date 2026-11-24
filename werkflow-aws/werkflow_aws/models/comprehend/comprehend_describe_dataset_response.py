from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_dataset_properties import ComprehendDatasetProperties


class ComprehendDescribeDatasetResponse(BaseModel):
    DatasetProperties: ComprehendDatasetProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
