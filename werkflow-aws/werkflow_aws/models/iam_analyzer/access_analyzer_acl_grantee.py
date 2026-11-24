from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerAclGrantee(BaseModel):
    id: StrictStr | None = None
    uri: StrictStr | None = None
