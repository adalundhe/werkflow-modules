from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3JSONOutput(BaseModel):
    RecordDelimiter: StrictStr | None = None
