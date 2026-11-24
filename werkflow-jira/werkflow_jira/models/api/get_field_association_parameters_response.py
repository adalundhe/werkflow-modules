from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_association_parameters import FieldAssociationParameters
from .work_type_parameters import WorkTypeParameters


class GetFieldAssociationParametersResponse(BaseModel):
    fieldId: StrictStr | None = None
    parameters: FieldAssociationParameters | None = None
    workTypeParameters: list[WorkTypeParameters] | None = None
