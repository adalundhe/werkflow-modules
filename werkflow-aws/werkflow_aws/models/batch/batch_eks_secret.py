from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BatchEksSecret(BaseModel):
    secretName: StrictStr | None = None
    optional: StrictBool | None = None
