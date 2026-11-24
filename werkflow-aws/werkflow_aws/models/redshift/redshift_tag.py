from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
