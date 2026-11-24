from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_reference_data import FieldReferenceData
from .function_reference_data import FunctionReferenceData


class JQLReferenceData(BaseModel):
    jqlReservedWords: list[StrictStr] | None = None
    visibleFieldNames: list[FieldReferenceData] | None = None
    visibleFunctionNames: list[FunctionReferenceData] | None = None
