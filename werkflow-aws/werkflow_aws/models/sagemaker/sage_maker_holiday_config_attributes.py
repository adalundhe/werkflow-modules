from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHolidayConfigAttributes(BaseModel):
    CountryCode: StrictStr | None = None
