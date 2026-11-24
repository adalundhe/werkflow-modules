from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchAWSDomainInformation(BaseModel):
    OwnerId: StrictStr | None = None
    DomainName: StrictStr | None = None
    Region: StrictStr | None = None
