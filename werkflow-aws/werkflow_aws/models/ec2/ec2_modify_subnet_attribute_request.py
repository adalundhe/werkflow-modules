from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue


class EC2ModifySubnetAttributeRequest(BaseModel):
    SubnetId: StrictStr
    AssignIpv6AddressOnCreation: EC2AttributeBooleanValue | None = None
    MapPublicIpOnLaunch: EC2AttributeBooleanValue | None = None
    MapCustomerOwnedIpOnLaunch: EC2AttributeBooleanValue | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    EnableDns64: EC2AttributeBooleanValue | None = None
    PrivateDnsHostnameTypeOnLaunch: Literal['ip-name', 'resource-name'] | None = None
    EnableResourceNameDnsARecordOnLaunch: EC2AttributeBooleanValue | None = None
    EnableResourceNameDnsAAAARecordOnLaunch: EC2AttributeBooleanValue | None = None
    EnableLniAtDeviceIndex: StrictInt | None = None
    DisableLniAtDeviceIndex: EC2AttributeBooleanValue | None = None
