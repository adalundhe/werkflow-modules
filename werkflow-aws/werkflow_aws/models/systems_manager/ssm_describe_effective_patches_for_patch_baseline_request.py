from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMDescribeEffectivePatchesForPatchBaselineRequest(BaseModel):
    BaselineId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
