from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessSecurityConfigSummary(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    configVersion: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
