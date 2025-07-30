from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class AthenaListDatabasesRequest(BaseModel):
    CatalogName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    WorkGroup: StrictStr | None = None