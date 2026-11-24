from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontAliasICPRecordal(BaseModel):
    CNAME: StrictStr | None = None
    ICPRecordalStatus: StrictStr | None = None
