from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_data_deletion_job import PersonalizeDataDeletionJob


class PersonalizeDescribeDataDeletionJobResponse(BaseModel):
    dataDeletionJob: PersonalizeDataDeletionJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
