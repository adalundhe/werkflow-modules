from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_variant_status import SageMakerVariantStatus


class SageMakerProductionVariantStatus(BaseModel):
    Status: SageMakerVariantStatus | None = None
    StatusMessage: StrictStr | None = None
    StartTime: datetime.datetime | None = None
