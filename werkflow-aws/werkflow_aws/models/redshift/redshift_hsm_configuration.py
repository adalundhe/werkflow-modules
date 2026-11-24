from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftHsmConfiguration(BaseModel):
    HsmConfigurationIdentifier: StrictStr | None = None
    Description: StrictStr | None = None
    HsmIpAddress: StrictStr | None = None
    HsmPartitionName: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
