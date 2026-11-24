from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_repository_catalog_data import ECRPublicRepositoryCatalogData


class ECRPublicGetRepositoryCatalogDataResponse(BaseModel):
    catalogData: ECRPublicRepositoryCatalogData | None = None
    ResponseMetadata: dict[str, Any] | None = None
