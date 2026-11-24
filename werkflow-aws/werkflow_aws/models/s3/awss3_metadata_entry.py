from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3MetadataEntry(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
