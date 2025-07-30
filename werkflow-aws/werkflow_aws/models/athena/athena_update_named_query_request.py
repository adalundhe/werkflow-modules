from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaUpdateNamedQueryRequest(BaseModel):
    NamedQueryId: StrictStr
    Name: StrictStr
    Description: StrictStr | None = None
    QueryString: StrictStr