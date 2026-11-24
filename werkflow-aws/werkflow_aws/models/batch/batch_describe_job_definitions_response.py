from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_job_definition import BatchJobDefinition


class BatchDescribeJobDefinitionsResponse(BaseModel):
    jobDefinitions: list[BatchJobDefinition] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
