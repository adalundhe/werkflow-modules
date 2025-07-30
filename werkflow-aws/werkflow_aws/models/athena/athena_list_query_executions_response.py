from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaListQueryExecutionsResponse(BaseModel):
    QueryExectionIds: list[StrictStr]
    NextToken: StrictStr | None = None