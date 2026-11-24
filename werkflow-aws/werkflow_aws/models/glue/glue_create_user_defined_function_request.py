from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_user_defined_function_input import GlueUserDefinedFunctionInput


class GlueCreateUserDefinedFunctionRequest(BaseModel):
    DatabaseName: StrictStr
    FunctionInput: GlueUserDefinedFunctionInput
    CatalogId: StrictStr | None = None
