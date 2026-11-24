from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AthenaPreparedStatementModel(BaseModel):
    StatementName: StrictStr | None = None
    QueryStatement: StrictStr | None = None
    WorkGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
