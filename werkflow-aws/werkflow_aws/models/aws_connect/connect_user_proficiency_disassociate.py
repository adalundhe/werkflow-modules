from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserProficiencyDisassociate(BaseModel):
    AttributeName: StrictStr
    AttributeValue: StrictStr
