from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_additional_result_attribute_value import KendraAdditionalResultAttributeValue


class KendraAdditionalResultAttribute(BaseModel):
    Key: StrictStr | None = None
    ValueType: StrictStr | None = None
    Value: KendraAdditionalResultAttributeValue | None = None
