from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .fields_scheme_item_parameter import FieldsSchemeItemParameter
from .fields_scheme_item_work_type_parameter import FieldsSchemeItemWorkTypeParameter


class UpdateFieldSchemeParametersRequest(BaseModel):
    parameters: FieldsSchemeItemParameter | None = None
    schemeIds: list[StrictInt] | None = None
    workTypeParameters: list[FieldsSchemeItemWorkTypeParameter] | None = None
