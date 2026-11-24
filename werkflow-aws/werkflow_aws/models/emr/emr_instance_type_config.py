from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .emr_configuration import EMRConfiguration
from .emr_ebs_configuration import EMREbsConfiguration


class EMRInstanceTypeConfig(BaseModel):
    InstanceType: StrictStr
    WeightedCapacity: StrictInt | None = None
    BidPrice: StrictStr | None = None
    BidPriceAsPercentageOfOnDemandPrice: StrictFloat | StrictInt | None = None
    EbsConfiguration: EMREbsConfiguration | None = None
    Configurations: list[EMRConfiguration] | None = None
    CustomAmiId: StrictStr | None = None
    Priority: StrictFloat | StrictInt | None = None
