from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_dataset_import_job import PersonalizeDatasetImportJob


class PersonalizeDescribeDatasetImportJobResponse(BaseModel):
    datasetImportJob: PersonalizeDatasetImportJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
