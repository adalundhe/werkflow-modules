from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerModelCardSummary(BaseModel):
    ModelCardName: StrictStr | None = None
    ModelCardArn: StrictStr | None = None
    ModelCardStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
