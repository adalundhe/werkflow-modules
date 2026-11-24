from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .service_catalog_record_error import ServiceCatalogRecordError
from .service_catalog_record_tag import ServiceCatalogRecordTag


class ServiceCatalogRecordDetail(BaseModel):
    RecordId: StrictStr | None = None
    ProvisionedProductName: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
    ProvisionedProductType: StrictStr | None = None
    RecordType: StrictStr | None = None
    ProvisionedProductId: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    PathId: StrictStr | None = None
    RecordErrors: list[ServiceCatalogRecordError] | None = None
    RecordTags: list[ServiceCatalogRecordTag] | None = None
    LaunchRoleArn: StrictStr | None = None
