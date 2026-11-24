from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_repository import ECRRepository


class ECRDescribeRepositoriesResponse(BaseModel):
    repositories: list[ECRRepository] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
