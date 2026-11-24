from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3JSONOutputModel(BaseModel):
    RecordDelimiter: StrictStr | None = None
