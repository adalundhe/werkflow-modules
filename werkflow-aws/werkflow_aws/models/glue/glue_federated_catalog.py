from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFederatedCatalog(BaseModel):
    Identifier: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
