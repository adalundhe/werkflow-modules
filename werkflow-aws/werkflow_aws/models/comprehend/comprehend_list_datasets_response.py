from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_dataset_properties import ComprehendDatasetProperties


class ComprehendListDatasetsResponse(BaseModel):
    DatasetPropertiesList: list[ComprehendDatasetProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
