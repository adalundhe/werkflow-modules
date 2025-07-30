from pydantic import (
    BaseModel,
    StrictStr
)
from .athena_data_catalog_type import AthenaDataCatalogType
from .athena_tag import AthenaTag


class AthenaCreateDataCatalogRequest(BaseModel):
    Name: StrictStr
    Type: AthenaDataCatalogType
    Description: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    Tags: list[AthenaTag] | None = None