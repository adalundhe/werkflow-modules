from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDataLakeAccessPropertiesOutput(BaseModel):
    DataLakeAccess: StrictBool | None = None
    DataTransferRole: StrictStr | None = None
    KmsKey: StrictStr | None = None
    ManagedWorkgroupName: StrictStr | None = None
    ManagedWorkgroupStatus: StrictStr | None = None
    RedshiftDatabaseName: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CatalogType: StrictStr | None = None
