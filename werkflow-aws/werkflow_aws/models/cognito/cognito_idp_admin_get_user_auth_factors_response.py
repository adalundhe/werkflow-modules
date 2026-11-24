from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminGetUserAuthFactorsResponse(BaseModel):
    Username: StrictStr | None = None
    PreferredMfaSetting: StrictStr | None = None
    UserMFASettingList: list[StrictStr] | None = None
    ConfiguredUserAuthFactors: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
