from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2ApiMapping(BaseModel):
    ApiId: StrictStr | None = None
    ApiMappingId: StrictStr | None = None
    ApiMappingKey: StrictStr | None = None
    Stage: StrictStr | None = None
