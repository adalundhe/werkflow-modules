from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDescribeJobSchemaVersionResponse(BaseModel):
    JobCategory: StrictStr | None = None
    JobConfigSchemaVersion: StrictStr | None = None
    JobConfigSchema: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
