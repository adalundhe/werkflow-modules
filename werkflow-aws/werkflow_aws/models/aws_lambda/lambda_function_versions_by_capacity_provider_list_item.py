from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFunctionVersionsByCapacityProviderListItem(BaseModel):
    FunctionArn: StrictStr | None = None
    State: StrictStr | None = None
