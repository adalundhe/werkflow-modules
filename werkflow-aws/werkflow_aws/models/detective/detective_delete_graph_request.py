from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveDeleteGraphRequest(BaseModel):
    GraphArn: StrictStr
