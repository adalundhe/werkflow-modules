from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchAccessPoliciesStatus(BaseModel):
    Options: StrictStr | None = None
    Status: CloudSearchOptionStatus | None = None
