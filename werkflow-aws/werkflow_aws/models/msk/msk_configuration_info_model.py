from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKConfigurationInfoModel(BaseModel):
    Arn: StrictStr | None = None
    Revision: StrictInt | None = None
