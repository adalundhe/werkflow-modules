from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeServicesRequest(BaseModel):
    serviceCodeList: list[StrictStr] | None = None
    language: StrictStr | None = None
    dryRun: StrictBool | None = None
