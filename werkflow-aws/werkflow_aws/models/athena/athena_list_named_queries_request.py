from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class AthenaListNamedQueriesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    WorkGroup: StrictStr | None = None