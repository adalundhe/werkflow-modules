from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAssetFormEntry(BaseModel):
    FormTypeId: StrictStr | None = None
    Content: StrictStr | None = None
