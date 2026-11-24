from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractGetProjectRequest(BaseModel):
    ProjectArn: StrictStr
