from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_context_source import SageMakerContextSource
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateContextRequest(BaseModel):
    ContextName: StrictStr
    Source: SageMakerContextSource
    ContextType: StrictStr
    Description: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    Tags: list[SageMakerTagModel] | None = None
