from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingDescribeRegistrationFieldValuesRequest(BaseModel):
    RegistrationId: StrictStr
    VersionNumber: StrictInt | None = None
    SectionPath: StrictStr | None = None
    FieldPaths: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
