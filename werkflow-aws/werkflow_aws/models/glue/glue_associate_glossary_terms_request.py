from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAssociateGlossaryTermsRequest(BaseModel):
    AssetIdentifier: StrictStr
    GlossaryTermIdentifiers: list[StrictStr]
    IterableFormName: StrictStr | None = None
    ItemIdentifier: StrictStr | None = None
    ClientToken: StrictStr | None = None
