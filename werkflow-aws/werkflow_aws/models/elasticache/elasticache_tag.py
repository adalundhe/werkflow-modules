from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElasticacheTag(BaseModel):
    Key: StrictStr
    Value: StrictStr | None = None
