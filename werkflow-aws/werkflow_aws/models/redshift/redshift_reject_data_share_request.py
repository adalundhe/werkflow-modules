from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftRejectDataShareRequest(BaseModel):
    DataShareArn: StrictStr
