from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_aws_location import DataZoneAwsLocation
from .data_zone_configuration import DataZoneConfiguration
from .data_zone_connection_properties_patch import DataZoneConnectionPropertiesPatch


class DataZoneUpdateConnectionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    configurations: list[DataZoneConfiguration] | None = None
    description: StrictStr | None = None
    awsLocation: DataZoneAwsLocation | None = None
    props: DataZoneConnectionPropertiesPatch | None = None
