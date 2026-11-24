from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayRequestPolicyRuleMetaData(BaseModel):
    MetaDataKey: StrictStr | None = None
    MetaDataValue: StrictStr | None = None
