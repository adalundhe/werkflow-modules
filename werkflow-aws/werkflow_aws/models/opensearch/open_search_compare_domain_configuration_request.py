from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCompareDomainConfigurationRequest(BaseModel):
    SourceDomainArn: StrictStr
    TargetDomainArn: StrictStr
    Categories: list[StrictStr]
