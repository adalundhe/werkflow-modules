from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_advanced_field_selector import CloudTrailAdvancedFieldSelector


class CloudTrailAdvancedEventSelector(BaseModel):
    Name: StrictStr | None = None
    FieldSelectors: list[CloudTrailAdvancedFieldSelector] | None = None
