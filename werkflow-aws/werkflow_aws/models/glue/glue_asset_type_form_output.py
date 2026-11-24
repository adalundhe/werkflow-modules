from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAssetTypeFormOutput(BaseModel):
    FormTypeId: StrictStr | None = None
