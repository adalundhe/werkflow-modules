from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_customer_agreement import DirectConnectCustomerAgreement


class DirectConnectDescribeCustomerMetadataResponse(BaseModel):
    agreements: list[DirectConnectCustomerAgreement] | None = None
    nniPartnerType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
