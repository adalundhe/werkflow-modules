from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSerDeInfo(BaseModel):
    Name: StrictStr | None = None
    SerializationLibrary: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
