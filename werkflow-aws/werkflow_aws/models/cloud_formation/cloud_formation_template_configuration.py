from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationTemplateConfiguration(BaseModel):
    DeletionPolicy: StrictStr | None = None
    UpdateReplacePolicy: StrictStr | None = None
