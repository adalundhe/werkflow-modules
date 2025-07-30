from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaDeletePreparedStatementRequest(BaseModel):
    StatementName: StrictStr
    WorkGroup: StrictStr