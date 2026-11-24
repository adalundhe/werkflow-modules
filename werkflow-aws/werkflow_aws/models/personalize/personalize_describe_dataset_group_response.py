from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_dataset_group import PersonalizeDatasetGroup


class PersonalizeDescribeDatasetGroupResponse(BaseModel):
    datasetGroup: PersonalizeDatasetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
