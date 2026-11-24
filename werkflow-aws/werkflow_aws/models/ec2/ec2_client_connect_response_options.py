from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_client_vpn_endpoint_attribute_status import EC2ClientVpnEndpointAttributeStatus


class EC2ClientConnectResponseOptions(BaseModel):
    Enabled: StrictBool | None = None
    LambdaFunctionArn: StrictStr | None = None
    Status: EC2ClientVpnEndpointAttributeStatus | None = None
