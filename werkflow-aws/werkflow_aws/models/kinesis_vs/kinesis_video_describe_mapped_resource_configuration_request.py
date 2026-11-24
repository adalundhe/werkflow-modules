from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoDescribeMappedResourceConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
