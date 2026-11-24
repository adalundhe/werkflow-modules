from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPDcrConfigurationType(BaseModel):
    EnableStatus: StrictStr | None = None
    OpenDcrEnabled: StrictBool | None = None
    AuthenticatedGrantTypes: list[StrictStr] | None = None
    OpenDcrGrantTypes: list[StrictStr] | None = None
    AllowedScopes: list[StrictStr] | None = None
