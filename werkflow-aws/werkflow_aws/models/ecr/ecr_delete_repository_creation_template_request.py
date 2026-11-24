from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRDeleteRepositoryCreationTemplateRequest(BaseModel):
    prefix: StrictStr
