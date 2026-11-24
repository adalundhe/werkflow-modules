from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSMetadataModelReference(BaseModel):
    MetadataModelName: StrictStr | None = None
    SelectionRules: StrictStr | None = None
