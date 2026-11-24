from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetImageFindingsRequest(BaseModel):
    ImageId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
