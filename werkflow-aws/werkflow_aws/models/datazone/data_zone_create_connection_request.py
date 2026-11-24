from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_aws_location import DataZoneAwsLocation
from .data_zone_configuration import DataZoneConfiguration
from .data_zone_connection_properties_input import DataZoneConnectionPropertiesInput


class DataZoneCreateConnectionRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    awsLocation: DataZoneAwsLocation | None = None
    clientToken: StrictStr | None = None
    configurations: list[DataZoneConfiguration] | None = None
    description: StrictStr | None = None
    environmentIdentifier: StrictStr | None = None
    props: DataZoneConnectionPropertiesInput | None = None
    enableTrustedIdentityPropagation: StrictBool | None = None
    scope: Literal['DOMAIN', 'PROJECT'] | None = None
