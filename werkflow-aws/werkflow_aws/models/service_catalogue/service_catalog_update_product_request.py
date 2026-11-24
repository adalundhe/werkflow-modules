from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_source_connection import ServiceCatalogSourceConnection
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogUpdateProductRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    Description: StrictStr | None = None
    Distributor: StrictStr | None = None
    SupportDescription: StrictStr | None = None
    SupportEmail: StrictStr | None = None
    SupportUrl: StrictStr | None = None
    AddTags: list[ServiceCatalogTag] | None = None
    RemoveTags: list[StrictStr] | None = None
    SourceConnection: ServiceCatalogSourceConnection | None = None
