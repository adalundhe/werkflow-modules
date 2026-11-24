from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaListNamedQueriesResponse(BaseModel):
    NamedQueryIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
