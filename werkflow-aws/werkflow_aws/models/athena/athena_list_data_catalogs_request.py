from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class AthenaListDataCatalogsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    WorkGroup: StrictStr | None = None