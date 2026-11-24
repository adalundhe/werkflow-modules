from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruAnomalySourceMetadata(BaseModel):
    Source: StrictStr | None = None
    SourceResourceName: StrictStr | None = None
    SourceResourceType: StrictStr | None = None
