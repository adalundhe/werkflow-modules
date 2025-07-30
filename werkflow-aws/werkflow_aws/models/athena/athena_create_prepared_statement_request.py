from pydantic import (
    BaseModel,
    StrictStr,
)

class AthenaCreatePreparedStatementRequest(BaseModel):
    StatementName: StrictStr
    WorkGroup: StrictStr
    QueryStatement: StrictStr
    Description: StrictStr | None = None