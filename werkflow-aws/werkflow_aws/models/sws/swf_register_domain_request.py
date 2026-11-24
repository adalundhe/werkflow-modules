from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_resource_tag import SWFResourceTag


class SWFRegisterDomainRequest(BaseModel):
    name: StrictStr
    workflowExecutionRetentionPeriodInDays: StrictStr
    description: StrictStr | None = None
    tags: list[SWFResourceTag] | None = None
