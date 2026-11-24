from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_module_info import CloudFormationModuleInfo
from .cloud_formation_resource_change_detail import CloudFormationResourceChangeDetail
from .cloud_formation_resource_drift_ignored_attribute import CloudFormationResourceDriftIgnoredAttribute


class CloudFormationResourceChange(BaseModel):
    PolicyAction: StrictStr | None = None
    Action: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Replacement: StrictStr | None = None
    Scope: list[StrictStr] | None = None
    ResourceDriftStatus: StrictStr | None = None
    ResourceDriftIgnoredAttributes: list[CloudFormationResourceDriftIgnoredAttribute] | None = None
    Details: list[CloudFormationResourceChangeDetail] | None = None
    ChangeSetId: StrictStr | None = None
    ModuleInfo: CloudFormationModuleInfo | None = None
    BeforeContext: StrictStr | None = None
    AfterContext: StrictStr | None = None
    PreviousDeploymentContext: StrictStr | None = None
