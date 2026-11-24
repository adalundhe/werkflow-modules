from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .service_catalog_source_connection_parameters import ServiceCatalogSourceConnectionParameters


class ServiceCatalogSourceConnection(BaseModel):
    ConnectionParameters: ServiceCatalogSourceConnectionParameters
    Type: Literal['CODESTAR'] | None = None
