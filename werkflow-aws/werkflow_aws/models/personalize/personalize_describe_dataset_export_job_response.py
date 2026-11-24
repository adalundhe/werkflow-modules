from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_dataset_export_job import PersonalizeDatasetExportJob


class PersonalizeDescribeDatasetExportJobResponse(BaseModel):
    datasetExportJob: PersonalizeDatasetExportJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
