from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_dataset_summary import PersonalizeDatasetSummary


class PersonalizeListDatasetsResponse(BaseModel):
    datasets: list[PersonalizeDatasetSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
