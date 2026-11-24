from __future__ import annotations
from pydantic import BaseModel
from .ses_vdm_attributes import SESVdmAttributes


class SESPutAccountVdmAttributesRequest(BaseModel):
    VdmAttributes: SESVdmAttributes
