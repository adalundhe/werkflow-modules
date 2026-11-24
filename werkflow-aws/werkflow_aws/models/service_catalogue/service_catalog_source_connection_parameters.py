from __future__ import annotations
from pydantic import BaseModel
from .service_catalog_code_star_parameters import ServiceCatalogCodeStarParameters


class ServiceCatalogSourceConnectionParameters(BaseModel):
    CodeStar: ServiceCatalogCodeStarParameters | None = None
