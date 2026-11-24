from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDomainInfo(BaseModel):
    DomainName: StrictStr | None = None
    EngineType: StrictStr | None = None
