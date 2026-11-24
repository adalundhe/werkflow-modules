from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_range import AppFlowRange


class AppFlowFieldTypeDetails(BaseModel):
    fieldType: StrictStr | None = None
    filterOperators: list[StrictStr] | None = None
    supportedValues: list[StrictStr] | None = None
    valueRegexPattern: StrictStr | None = None
    supportedDateFormat: StrictStr | None = None
    fieldValueRange: AppFlowRange | None = None
    fieldLengthRange: AppFlowRange | None = None
