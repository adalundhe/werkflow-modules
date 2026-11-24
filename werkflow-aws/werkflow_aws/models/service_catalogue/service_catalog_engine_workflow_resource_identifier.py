from __future__ import annotations
from pydantic import BaseModel
from .service_catalog_unique_tag_resource_identifier import ServiceCatalogUniqueTagResourceIdentifier


class ServiceCatalogEngineWorkflowResourceIdentifier(BaseModel):
    UniqueTag: ServiceCatalogUniqueTagResourceIdentifier | None = None
