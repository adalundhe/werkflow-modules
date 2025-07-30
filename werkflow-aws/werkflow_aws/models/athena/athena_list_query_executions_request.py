from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class AthenaListQueryExecutionsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    WorkGroup: StrictStr | None = None