from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_data_catalog_type import AthenaDataCatalogType


class AthenaUpdateDataCatalog(BaseModel):
    Name: StrictStr
    Type: AthenaDataCatalogType
    Description: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None