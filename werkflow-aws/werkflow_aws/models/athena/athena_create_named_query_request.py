from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaCreateNamedQueryRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Database: StrictStr
    QueryString: StrictStr
    ClientRequestToken: StrictStr | None = None
    WorkGroup: StrictStr | None = None