from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_extension_health_issue import SageMakerExtensionHealthIssue


class SageMakerExtensionHealth(BaseModel):
    Issues: list[SageMakerExtensionHealthIssue] | None = None
