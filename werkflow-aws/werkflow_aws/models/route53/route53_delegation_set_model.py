from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DelegationSetModel(BaseModel):
    Id: StrictStr | None = None
    CallerReference: StrictStr | None = None
    NameServers: list[StrictStr] | None = None
