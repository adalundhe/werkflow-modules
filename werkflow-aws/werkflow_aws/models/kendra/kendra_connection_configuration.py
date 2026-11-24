from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraConnectionConfiguration(BaseModel):
    DatabaseHost: StrictStr | None = None
    DatabasePort: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    SecretArn: StrictStr | None = None
