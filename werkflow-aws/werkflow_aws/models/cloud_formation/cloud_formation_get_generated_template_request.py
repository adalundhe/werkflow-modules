from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationGetGeneratedTemplateRequest(BaseModel):
    GeneratedTemplateName: StrictStr
    Format: Literal['JSON', 'YAML'] | None = None
