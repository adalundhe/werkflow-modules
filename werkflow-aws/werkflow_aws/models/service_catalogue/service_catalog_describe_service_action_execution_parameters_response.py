from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_execution_parameter import ServiceCatalogExecutionParameter


class ServiceCatalogDescribeServiceActionExecutionParametersResponse(BaseModel):
    ServiceActionParameters: list[ServiceCatalogExecutionParameter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
