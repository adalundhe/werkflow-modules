from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSGetSMSAttributesRequest(BaseModel):
    attributes: list[StrictStr] | None = None
