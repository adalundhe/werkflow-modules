from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CustomTemplateOptions(BaseModel):
    enableScreenDelegatedAdminSupport: StrictBool | None = None
    enableWorkflowDelegatedAdminSupport: StrictBool | None = None
