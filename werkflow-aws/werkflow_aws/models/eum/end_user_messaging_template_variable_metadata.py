from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingTemplateVariableMetadata(BaseModel):
    Type: StrictStr | None = None
    Required: StrictBool | None = None
    Description: StrictStr | None = None
    MaxLength: StrictInt | None = None
    MinValue: StrictInt | None = None
    MaxValue: StrictInt | None = None
    DefaultValue: StrictStr | None = None
    Pattern: StrictStr | None = None
    Sample: StrictStr | None = None
    Source: StrictStr | None = None
