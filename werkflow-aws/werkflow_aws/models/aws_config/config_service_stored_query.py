from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceStoredQuery(BaseModel):
    QueryId: StrictStr | None = None
    QueryArn: StrictStr | None = None
    QueryName: StrictStr | None = None
    Description: StrictStr | None = None
    Expression: StrictStr | None = None
