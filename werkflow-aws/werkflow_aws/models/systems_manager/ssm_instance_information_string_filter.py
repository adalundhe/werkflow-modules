from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInstanceInformationStringFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
