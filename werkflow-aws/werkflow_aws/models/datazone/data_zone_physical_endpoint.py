from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .data_zone_aws_location import DataZoneAwsLocation
from .data_zone_glue_connection import DataZoneGlueConnection


class DataZonePhysicalEndpoint(BaseModel):
    awsLocation: DataZoneAwsLocation | None = None
    glueConnectionName: StrictStr | None = None
    glueConnectionNames: list[StrictStr] | None = None
    glueConnection: DataZoneGlueConnection | None = None
    enableTrustedIdentityPropagation: StrictBool | None = None
    host: StrictStr | None = None
    port: StrictInt | None = None
    protocol: StrictStr | None = None
    stage: StrictStr | None = None
