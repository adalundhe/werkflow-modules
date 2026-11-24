from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKConfigurationInfo(BaseModel):
    Arn: StrictStr | None = None
    Revision: StrictInt | None = None
