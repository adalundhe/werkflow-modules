from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGlobalInferenceGatewayMember(BaseModel):
    Name: StrictStr | None = None
    Namespace: StrictStr | None = None
    ClusterArn: StrictStr | None = None
