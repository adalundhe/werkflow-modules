from pydantic import (
    BaseModel,
    StrictStr
)
from .athena_connection_type import AthenaConnectionType
from .athena_data_catalog_status import AthenaDataCatalogStatus
from .athena_data_catalog_type import AthenaDataCatalogType


class AthenaDataCatalog(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Type: AthenaDataCatalogType
    Parameters: dict[StrictStr, StrictStr] | None = None
    Status: AthenaDataCatalogStatus
    ConnectionType: AthenaConnectionType
    Error: StrictStr | None = None