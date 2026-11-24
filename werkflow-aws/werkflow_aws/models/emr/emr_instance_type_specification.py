from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .emr_configuration import EMRConfiguration
from .emr_ebs_block_device import EMREbsBlockDevice


class EMRInstanceTypeSpecification(BaseModel):
    InstanceType: StrictStr | None = None
    WeightedCapacity: StrictInt | None = None
    BidPrice: StrictStr | None = None
    BidPriceAsPercentageOfOnDemandPrice: StrictFloat | StrictInt | None = None
    Configurations: list[EMRConfiguration] | None = None
    EbsBlockDevices: list[EMREbsBlockDevice] | None = None
    EbsOptimized: StrictBool | None = None
    CustomAmiId: StrictStr | None = None
    Priority: StrictFloat | StrictInt | None = None
