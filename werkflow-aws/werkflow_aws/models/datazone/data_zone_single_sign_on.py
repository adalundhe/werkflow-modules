from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSingleSignOn(BaseModel):
    type: StrictStr | None = None
    userAssignment: StrictStr | None = None
    idcInstanceArn: StrictStr | None = None
