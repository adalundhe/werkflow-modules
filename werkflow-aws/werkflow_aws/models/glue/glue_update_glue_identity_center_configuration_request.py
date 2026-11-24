from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueUpdateGlueIdentityCenterConfigurationRequest(BaseModel):
    Scopes: list[StrictStr] | None = None
    UserBackgroundSessionsEnabled: StrictBool | None = None
