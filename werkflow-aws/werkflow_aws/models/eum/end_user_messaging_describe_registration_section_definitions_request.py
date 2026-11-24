from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingDescribeRegistrationSectionDefinitionsRequest(BaseModel):
    RegistrationType: StrictStr
    SectionPaths: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
