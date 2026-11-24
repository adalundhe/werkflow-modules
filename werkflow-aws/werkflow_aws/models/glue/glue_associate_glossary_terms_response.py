from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueAssociateGlossaryTermsResponse(BaseModel):
    AssetId: StrictStr | None = None
    IterableFormName: StrictStr | None = None
    ItemId: StrictStr | None = None
    GlossaryTerms: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
