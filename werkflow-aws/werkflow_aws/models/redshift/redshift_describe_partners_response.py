from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_partner_integration_info import RedshiftPartnerIntegrationInfo


class RedshiftDescribePartnersResponse(BaseModel):
    PartnerIntegrationInfoList: list[RedshiftPartnerIntegrationInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
