from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MacieUpdateOrganizationConfigurationRequest(BaseModel):
    autoEnable: StrictBool
