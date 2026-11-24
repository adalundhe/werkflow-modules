from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockMetadataAttributeSchema(BaseModel):
    key: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
