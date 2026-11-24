from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSEndpointSetting(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    EnumValues: list[StrictStr] | None = None
    Sensitive: StrictBool | None = None
    Units: StrictStr | None = None
    Applicability: StrictStr | None = None
    IntValueMin: StrictInt | None = None
    IntValueMax: StrictInt | None = None
    DefaultValue: StrictStr | None = None
