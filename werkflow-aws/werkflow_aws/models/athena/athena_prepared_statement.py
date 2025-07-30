import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaPreparedStatement(BaseModel):
    StatementName: StrictStr
    QueryStatement: StrictStr | None = None
    WorkGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    LastModifiedTime: datetime.datetime