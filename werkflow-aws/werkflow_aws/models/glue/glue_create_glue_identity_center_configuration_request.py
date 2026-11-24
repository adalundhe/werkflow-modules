from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCreateGlueIdentityCenterConfigurationRequest(BaseModel):
    InstanceArn: StrictStr
    Scopes: list[StrictStr] | None = None
    UserBackgroundSessionsEnabled: StrictBool | None = None
