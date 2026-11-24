from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_job_config_schema_version_summary import SageMakerJobConfigSchemaVersionSummary


class SageMakerListJobSchemaVersionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    JobConfigSchemas: list[SageMakerJobConfigSchemaVersionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
