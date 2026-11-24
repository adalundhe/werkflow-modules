from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowLambdaConnectorProvisioningConfig(BaseModel):
    lambdaArn: StrictStr | None = None
