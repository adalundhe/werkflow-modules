from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDataTableLockVersion(BaseModel):
    DataTable: StrictStr | None = None
    Attribute: StrictStr | None = None
    PrimaryValues: StrictStr | None = None
    Value: StrictStr | None = None
