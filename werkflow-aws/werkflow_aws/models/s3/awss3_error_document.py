from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3ErrorDocument(BaseModel):
    Key: StrictStr | None = None
