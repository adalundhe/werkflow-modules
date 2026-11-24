from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchDescribeJobDefinitionsRequest(BaseModel):
    jobDefinitions: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    jobDefinitionName: StrictStr | None = None
    status: StrictStr | None = None
    nextToken: StrictStr | None = None
