from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2RequestBodyAssociatedResourceTypeConfig(BaseModel):
    DefaultSizeInspectionLimit: StrictStr | None = None
