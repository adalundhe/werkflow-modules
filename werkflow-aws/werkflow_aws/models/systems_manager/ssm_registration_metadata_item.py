from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMRegistrationMetadataItem(BaseModel):
    Key: StrictStr
    Value: StrictStr
