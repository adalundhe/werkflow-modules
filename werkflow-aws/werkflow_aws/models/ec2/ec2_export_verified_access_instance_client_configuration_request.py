from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ExportVerifiedAccessInstanceClientConfigurationRequest(BaseModel):
    VerifiedAccessInstanceId: StrictStr
    DryRun: StrictBool | None = None
