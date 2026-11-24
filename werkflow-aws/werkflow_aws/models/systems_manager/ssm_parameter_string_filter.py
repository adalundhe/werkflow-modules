from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMParameterStringFilter(BaseModel):
    Key: StrictStr
    Option: StrictStr | None = None
    Values: list[StrictStr] | None = None
