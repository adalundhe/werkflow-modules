from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSetSMSAttributesRequest(BaseModel):
    attributes: dict[StrictStr, StrictStr]
