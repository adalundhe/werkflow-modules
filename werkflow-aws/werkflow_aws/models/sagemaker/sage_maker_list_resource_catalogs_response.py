from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_resource_catalog import SageMakerResourceCatalog


class SageMakerListResourceCatalogsResponse(BaseModel):
    ResourceCatalogs: list[SageMakerResourceCatalog] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
