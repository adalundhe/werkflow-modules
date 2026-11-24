from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGlobalInferenceGatewayMemberSummary(BaseModel):
    Name: StrictStr | None = None
    Namespace: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
