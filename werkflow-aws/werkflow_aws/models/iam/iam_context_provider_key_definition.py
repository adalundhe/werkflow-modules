from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMContextProviderKeyDefinition(BaseModel):
    SourceKey: StrictStr | None = None
    TargetKey: StrictStr | None = None
