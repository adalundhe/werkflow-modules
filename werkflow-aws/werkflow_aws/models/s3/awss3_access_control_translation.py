from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3AccessControlTranslation(BaseModel):
    Owner: StrictStr | None = None
