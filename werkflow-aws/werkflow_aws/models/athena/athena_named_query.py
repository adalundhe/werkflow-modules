from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaNamedQuery(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Database: StrictStr
    QueryString: StrictStr
    NamedQueryId: StrictStr
    WorkGroup: StrictStr | None = None