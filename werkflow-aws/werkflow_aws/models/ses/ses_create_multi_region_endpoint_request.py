from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_details import SESDetails
from .ses_tag import SESTag


class SESCreateMultiRegionEndpointRequest(BaseModel):
    EndpointName: StrictStr
    Details: SESDetails
    Tags: list[SESTag] | None = None
