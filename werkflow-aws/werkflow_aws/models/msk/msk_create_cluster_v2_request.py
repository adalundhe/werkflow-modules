from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_provisioned_request import MSKProvisionedRequest
from .msk_serverless_request import MSKServerlessRequest


class MSKCreateClusterV2Request(BaseModel):
    ClusterName: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
    Provisioned: MSKProvisionedRequest | None = None
    Serverless: MSKServerlessRequest | None = None
