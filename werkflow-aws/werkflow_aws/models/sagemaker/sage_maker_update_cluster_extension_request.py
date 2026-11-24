from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateClusterExtensionRequest(BaseModel):
    ClusterArn: StrictStr
    ExtensionArn: StrictStr
    ExtensionVersion: StrictStr | None = None
    ConfigurationValues: StrictStr | None = None
    ClientToken: StrictStr | None = None
