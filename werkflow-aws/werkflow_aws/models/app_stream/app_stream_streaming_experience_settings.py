from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStreamingExperienceSettings(BaseModel):
    PreferredProtocol: StrictStr | None = None
