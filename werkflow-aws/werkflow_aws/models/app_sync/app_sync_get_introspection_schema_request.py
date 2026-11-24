from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class AppSyncGetIntrospectionSchemaRequest(BaseModel):
    apiId: StrictStr
    format: Literal['SDL', 'JSON']
    includeDirectives: StrictBool | None = None
