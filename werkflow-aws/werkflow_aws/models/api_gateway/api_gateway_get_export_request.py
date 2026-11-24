from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetExportRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
    exportType: StrictStr
    parameters: dict[StrictStr, StrictStr] | None = None
    accepts: StrictStr | None = None
