from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetDataCatalogRequest(BaseModel):
    Name: StrictStr
    WorkGroup: StrictStr | None = None