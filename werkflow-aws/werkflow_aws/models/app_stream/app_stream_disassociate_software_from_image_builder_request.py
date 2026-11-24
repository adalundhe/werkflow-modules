from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDisassociateSoftwareFromImageBuilderRequest(BaseModel):
    ImageBuilderName: StrictStr
    SoftwareNames: list[StrictStr]
