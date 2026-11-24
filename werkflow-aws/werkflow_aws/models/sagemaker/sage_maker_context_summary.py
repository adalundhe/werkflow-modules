from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_context_source import SageMakerContextSource


class SageMakerContextSummary(BaseModel):
    ContextArn: StrictStr | None = None
    ContextName: StrictStr | None = None
    Source: SageMakerContextSource | None = None
    ContextType: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
