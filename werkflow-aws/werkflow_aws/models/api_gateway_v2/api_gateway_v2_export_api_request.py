from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayV2ExportApiRequest(BaseModel):
    ApiId: StrictStr
    OutputType: Literal['YAML', 'JSON']
    Specification: Literal['OAS30']
    ExportVersion: StrictStr | None = None
    IncludeExtensions: StrictBool | None = None
    StageName: StrictStr | None = None
