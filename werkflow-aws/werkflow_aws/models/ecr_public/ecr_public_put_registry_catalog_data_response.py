from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_registry_catalog_data import ECRPublicRegistryCatalogData


class ECRPublicPutRegistryCatalogDataResponse(BaseModel):
    registryCatalogData: ECRPublicRegistryCatalogData | None = None
    ResponseMetadata: dict[str, Any] | None = None
