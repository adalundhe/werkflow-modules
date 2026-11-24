from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaCapacityProviderPermissionsConfig(BaseModel):
    CapacityProviderOperatorRoleArn: StrictStr | None = None
