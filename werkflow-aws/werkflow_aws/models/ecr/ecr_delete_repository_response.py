from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_repository import ECRRepository


class ECRDeleteRepositoryResponse(BaseModel):
    repository: ECRRepository | None = None
    ResponseMetadata: dict[str, Any] | None = None
