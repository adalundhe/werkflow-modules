from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsMetadataFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
