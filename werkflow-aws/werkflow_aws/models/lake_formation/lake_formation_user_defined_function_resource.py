from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_user_defined_function_wildcard import LakeFormationUserDefinedFunctionWildcard


class LakeFormationUserDefinedFunctionResource(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Name: StrictStr | None = None
    UserDefinedFunctionWildcard: LakeFormationUserDefinedFunctionWildcard | None = None
