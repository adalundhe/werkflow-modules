from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractDeleteProjectRequest(BaseModel):
    ProjectArn: StrictStr
