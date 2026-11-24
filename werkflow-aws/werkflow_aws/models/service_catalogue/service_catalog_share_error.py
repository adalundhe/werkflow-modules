from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogShareError(BaseModel):
    Accounts: list[StrictStr] | None = None
    Message: StrictStr | None = None
    Error: StrictStr | None = None
