from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraLabelPropertiesInputJackson1(BaseModel):
    color: StrictStr | None = None
    name: StrictStr | None = None
