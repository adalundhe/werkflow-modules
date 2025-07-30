from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetPreparedStatementRequest(BaseModel):
    StatementName: StrictStr
    WorkGroup: StrictStr | None = None