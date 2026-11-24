from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSparkEmrPropertiesPatch(BaseModel):
    computeArn: StrictStr | None = None
    instanceProfileArn: StrictStr | None = None
    javaVirtualEnv: StrictStr | None = None
    logUri: StrictStr | None = None
    pythonVirtualEnv: StrictStr | None = None
    runtimeRole: StrictStr | None = None
    trustedCertificatesS3Uri: StrictStr | None = None
    managedEndpointArn: StrictStr | None = None
