from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ListImagesInRecycleBinRequest(BaseModel):
    ImageIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
