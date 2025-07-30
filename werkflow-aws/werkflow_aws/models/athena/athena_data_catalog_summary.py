from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_data_catalog_type import AthenaDataCatalogType
from .athena_data_catalog_status import AthenaDataCatalogStatus
from .athena_connection_type import AthenaConnectionType


class AthenaDataCatalogSummary(BaseModel):
    CatalogName: StrictStr
    Type: AthenaDataCatalogType
    Status: AthenaDataCatalogStatus
    ConnectionType: AthenaConnectionType
    Error: StrictStr | None = None