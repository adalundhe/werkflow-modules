from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_data_protection import WAFv2DataProtection


class WAFv2DataProtectionConfig(BaseModel):
    DataProtections: list[WAFv2DataProtection] | None = None
