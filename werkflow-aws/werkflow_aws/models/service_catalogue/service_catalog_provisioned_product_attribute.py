from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogProvisionedProductAttribute(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
    Id: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    LastRecordId: StrictStr | None = None
    LastProvisioningRecordId: StrictStr | None = None
    LastSuccessfulProvisioningRecordId: StrictStr | None = None
    Tags: list[ServiceCatalogTag] | None = None
    PhysicalId: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProductName: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ProvisioningArtifactName: StrictStr | None = None
    UserArn: StrictStr | None = None
    UserArnSession: StrictStr | None = None
