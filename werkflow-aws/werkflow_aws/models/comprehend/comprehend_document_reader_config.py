from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDocumentReaderConfig(BaseModel):
    DocumentReadAction: StrictStr | None = None
    DocumentReadMode: StrictStr | None = None
    FeatureTypes: list[StrictStr] | None = None
