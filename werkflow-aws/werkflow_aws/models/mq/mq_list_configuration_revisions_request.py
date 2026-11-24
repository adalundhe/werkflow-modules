from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MQListConfigurationRevisionsRequest(BaseModel):
    ConfigurationId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
