from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_shape_conditional_format import QuickSightShapeConditionalFormat


class QuickSightFilledMapShapeConditionalFormatting(BaseModel):
    FieldId: StrictStr | None = None
    Format: QuickSightShapeConditionalFormat | None = None
