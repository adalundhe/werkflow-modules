from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionGetCelebrityInfoRequest(BaseModel):
    Id: StrictStr
