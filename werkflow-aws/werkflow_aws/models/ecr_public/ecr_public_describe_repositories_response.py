from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_public_repository import ECRPublicRepository


class ECRPublicDescribeRepositoriesResponse(BaseModel):
    repositories: list[ECRPublicRepository] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
