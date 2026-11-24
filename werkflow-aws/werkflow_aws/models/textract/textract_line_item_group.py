from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .textract_line_item_fields import TextractLineItemFields


class TextractLineItemGroup(BaseModel):
    LineItemGroupIndex: StrictInt | None = None
    LineItems: list[TextractLineItemFields] | None = None
