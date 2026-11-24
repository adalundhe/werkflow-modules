from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeAddonConfigurationRequest(BaseModel):
    addonName: StrictStr
    addonVersion: StrictStr
