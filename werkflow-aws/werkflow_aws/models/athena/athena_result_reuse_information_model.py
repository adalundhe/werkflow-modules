from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AthenaResultReuseInformationModel(BaseModel):
    ReusedPreviousResult: StrictBool | None = None
