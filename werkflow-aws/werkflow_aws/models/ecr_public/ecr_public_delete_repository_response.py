from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_repository import ECRPublicRepository


class ECRPublicDeleteRepositoryResponse(BaseModel):
    repository: ECRPublicRepository | None = None
    ResponseMetadata: dict[str, Any] | None = None
