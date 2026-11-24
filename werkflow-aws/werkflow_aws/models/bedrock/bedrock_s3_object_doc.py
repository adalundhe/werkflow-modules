from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockS3ObjectDoc(BaseModel):
    uri: StrictStr | None = None
