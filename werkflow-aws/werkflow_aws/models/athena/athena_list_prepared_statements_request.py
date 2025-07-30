from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class AthenaListPreparedStatementsRequest(BaseModel):
    WorkGroup: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None