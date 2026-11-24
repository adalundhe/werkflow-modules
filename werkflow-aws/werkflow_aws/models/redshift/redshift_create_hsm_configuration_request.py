from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateHsmConfigurationRequest(BaseModel):
    HsmConfigurationIdentifier: StrictStr
    Description: StrictStr
    HsmIpAddress: StrictStr
    HsmPartitionName: StrictStr
    HsmPartitionPassword: StrictStr
    HsmServerPublicCertificate: StrictStr
    Tags: list[RedshiftTag] | None = None
