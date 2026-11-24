from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_access_scope_path_request import EC2AccessScopePathRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateNetworkInsightsAccessScopeRequest(BaseModel):
    ClientToken: StrictStr
    MatchPaths: list[EC2AccessScopePathRequest] | None = None
    ExcludePaths: list[EC2AccessScopePathRequest] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
