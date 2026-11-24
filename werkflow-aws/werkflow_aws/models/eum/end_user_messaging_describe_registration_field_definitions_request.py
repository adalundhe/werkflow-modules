from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingDescribeRegistrationFieldDefinitionsRequest(BaseModel):
    RegistrationType: StrictStr
    SectionPath: StrictStr | None = None
    FieldPaths: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
