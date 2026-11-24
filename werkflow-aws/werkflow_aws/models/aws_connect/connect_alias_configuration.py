from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAliasConfiguration(BaseModel):
    EmailAddressId: StrictStr | None = None
