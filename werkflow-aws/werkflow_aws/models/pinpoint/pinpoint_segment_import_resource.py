from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointSegmentImportResource(BaseModel):
    ChannelCounts: dict[StrictStr, StrictInt] | None = None
    ExternalId: StrictStr | None = None
    Format: StrictStr | None = None
    RoleArn: StrictStr | None = None
    S3Url: StrictStr | None = None
    Size: StrictInt | None = None
