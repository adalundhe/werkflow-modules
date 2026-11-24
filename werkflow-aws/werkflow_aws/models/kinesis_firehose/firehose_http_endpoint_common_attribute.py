from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseHttpEndpointCommonAttribute(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValue: StrictStr | None = None
