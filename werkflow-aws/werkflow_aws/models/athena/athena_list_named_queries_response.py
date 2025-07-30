from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaListNamedQueriesResponse(BaseModel):
    NamedQueryIds: list[StrictStr]
    NextToken: StrictStr | None = None