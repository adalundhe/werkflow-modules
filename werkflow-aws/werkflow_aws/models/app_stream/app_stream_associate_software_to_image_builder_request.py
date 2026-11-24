from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAssociateSoftwareToImageBuilderRequest(BaseModel):
    ImageBuilderName: StrictStr
    SoftwareNames: list[StrictStr]
