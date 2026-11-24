from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyBackend(BaseModel):
    stackArn: StrictStr | None = None
