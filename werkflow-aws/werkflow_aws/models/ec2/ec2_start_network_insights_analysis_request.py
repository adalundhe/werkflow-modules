from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2StartNetworkInsightsAnalysisRequest(BaseModel):
    NetworkInsightsPathId: StrictStr
    ClientToken: StrictStr
    AdditionalAccounts: list[StrictStr] | None = None
    FilterInArns: list[StrictStr] | None = None
    FilterOutArns: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
