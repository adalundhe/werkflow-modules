from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_properties import ServiceCatalogProvisioningArtifactProperties
from .service_catalog_source_connection import ServiceCatalogSourceConnection
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogCreateProductRequest(BaseModel):
    Name: StrictStr
    Owner: StrictStr
    ProductType: Literal['CLOUD_FORMATION_TEMPLATE', 'MARKETPLACE', 'TERRAFORM_OPEN_SOURCE', 'TERRAFORM_CLOUD', 'EXTERNAL']
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    Description: StrictStr | None = None
    Distributor: StrictStr | None = None
    SupportDescription: StrictStr | None = None
    SupportEmail: StrictStr | None = None
    SupportUrl: StrictStr | None = None
    Tags: list[ServiceCatalogTag] | None = None
    ProvisioningArtifactParameters: ServiceCatalogProvisioningArtifactProperties | None = None
    SourceConnection: ServiceCatalogSourceConnection | None = None
