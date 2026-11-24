from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_parameter_declaration import CloudFormationParameterDeclaration
from .cloud_formation_resource_identifier_summary import CloudFormationResourceIdentifierSummary
from .cloud_formation_warnings import CloudFormationWarnings


class CloudFormationGetTemplateSummaryResponse(BaseModel):
    Parameters: list[CloudFormationParameterDeclaration] | None = None
    Description: StrictStr | None = None
    Capabilities: list[StrictStr] | None = None
    CapabilitiesReason: StrictStr | None = None
    ResourceTypes: list[StrictStr] | None = None
    Version: StrictStr | None = None
    Metadata: StrictStr | None = None
    DeclaredTransforms: list[StrictStr] | None = None
    ResourceIdentifierSummaries: list[CloudFormationResourceIdentifierSummary] | None = None
    Warnings: CloudFormationWarnings | None = None
    ResponseMetadata: dict[str, Any] | None = None
