from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_vdm_options import SESVdmOptions


class SESPutConfigurationSetVdmOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    VdmOptions: SESVdmOptions | None = None
