from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_repository import ECRPublicRepository
from .ecr_public_repository_catalog_data import ECRPublicRepositoryCatalogData


class ECRPublicCreateRepositoryResponse(BaseModel):
    repository: ECRPublicRepository | None = None
    catalogData: ECRPublicRepositoryCatalogData | None = None
    ResponseMetadata: dict[str, Any] | None = None
