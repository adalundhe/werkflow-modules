from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_managed_endpoint_credentials import DataZoneManagedEndpointCredentials
from .data_zone_username_password import DataZoneUsernamePassword


class DataZoneSparkEmrPropertiesOutput(BaseModel):
    computeArn: StrictStr | None = None
    credentials: DataZoneUsernamePassword | None = None
    credentialsExpiration: datetime.datetime | StrictStr | None = None
    governanceType: StrictStr | None = None
    instanceProfileArn: StrictStr | None = None
    javaVirtualEnv: StrictStr | None = None
    livyEndpoint: StrictStr | None = None
    logUri: StrictStr | None = None
    pythonVirtualEnv: StrictStr | None = None
    runtimeRole: StrictStr | None = None
    trustedCertificatesS3Uri: StrictStr | None = None
    certificateData: StrictStr | None = None
    managedEndpointArn: StrictStr | None = None
    managedEndpointCredentials: DataZoneManagedEndpointCredentials | None = None
