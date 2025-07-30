from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
)


class AthenaDeleteDataCatalogRequest(BaseModel):
    Name: StrictStr
    DeleteCatalogOnly: StrictBool = False