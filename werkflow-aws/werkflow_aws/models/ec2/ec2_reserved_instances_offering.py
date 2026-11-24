from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .ec2_pricing_detail import EC2PricingDetail
from .ec2_recurring_charge import EC2RecurringCharge


class EC2ReservedInstancesOffering(BaseModel):
    CurrencyCode: StrictStr | None = None
    InstanceTenancy: StrictStr | None = None
    Marketplace: StrictBool | None = None
    OfferingClass: StrictStr | None = None
    OfferingType: StrictStr | None = None
    PricingDetails: list[EC2PricingDetail] | None = None
    RecurringCharges: list[EC2RecurringCharge] | None = None
    Scope: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    ReservedInstancesOfferingId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Duration: StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    ProductDescription: StrictStr | None = None
