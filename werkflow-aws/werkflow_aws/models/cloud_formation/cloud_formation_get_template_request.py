from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationGetTemplateRequest(BaseModel):
    StackName: StrictStr | None = None
    ChangeSetName: StrictStr | None = None
    TemplateStage: Literal['Original', 'Processed'] | None = None
