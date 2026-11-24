from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_dataset_group_summary import PersonalizeDatasetGroupSummary


class PersonalizeListDatasetGroupsResponse(BaseModel):
    datasetGroups: list[PersonalizeDatasetGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
