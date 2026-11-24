from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAssetFormInput(BaseModel):
    FormTypeIdentifier: StrictStr | None = None
    Content: StrictStr | None = None
