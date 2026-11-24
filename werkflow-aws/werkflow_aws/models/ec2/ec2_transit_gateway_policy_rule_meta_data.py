from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayPolicyRuleMetaData(BaseModel):
    MetaDataKey: StrictStr | None = None
    MetaDataValue: StrictStr | None = None
