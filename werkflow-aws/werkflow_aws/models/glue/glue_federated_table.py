from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFederatedTable(BaseModel):
    Identifier: StrictStr | None = None
    DatabaseIdentifier: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
