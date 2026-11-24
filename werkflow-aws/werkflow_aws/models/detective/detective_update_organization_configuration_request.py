from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DetectiveUpdateOrganizationConfigurationRequest(BaseModel):
    GraphArn: StrictStr
    AutoEnable: StrictBool | None = None
