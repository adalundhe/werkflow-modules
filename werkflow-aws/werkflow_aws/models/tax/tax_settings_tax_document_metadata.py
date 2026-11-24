from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsTaxDocumentMetadata(BaseModel):
    taxDocumentAccessToken: StrictStr | None = None
    taxDocumentName: StrictStr | None = None
