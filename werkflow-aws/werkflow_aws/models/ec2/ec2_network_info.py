from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_default_connection_tracking_configuration import EC2DefaultConnectionTrackingConfiguration
from .ec2_efa_info import EC2EfaInfo
from .ec2_network_card_info import EC2NetworkCardInfo


class EC2NetworkInfo(BaseModel):
    NetworkPerformance: StrictStr | None = None
    MaximumNetworkInterfaces: StrictInt | None = None
    MaximumNetworkCards: StrictInt | None = None
    DefaultNetworkCardIndex: StrictInt | None = None
    NetworkCards: list[EC2NetworkCardInfo] | None = None
    Ipv4AddressesPerInterface: StrictInt | None = None
    Ipv6AddressesPerInterface: StrictInt | None = None
    Ipv6Supported: StrictBool | None = None
    EnaSupport: StrictStr | None = None
    EfaSupported: StrictBool | None = None
    EfaInfo: EC2EfaInfo | None = None
    EncryptionInTransitSupported: StrictBool | None = None
    EnaSrdSupported: StrictBool | None = None
    BandwidthWeightings: list[StrictStr] | None = None
    FlexibleEnaQueuesSupport: StrictStr | None = None
    ConnectionTrackingConfiguration: EC2DefaultConnectionTrackingConfiguration | None = None
    SecondaryNetworkSupported: StrictBool | None = None
    MaximumSecondaryNetworkInterfaces: StrictInt | None = None
    Ipv4AddressesPerSecondaryInterface: StrictInt | None = None
