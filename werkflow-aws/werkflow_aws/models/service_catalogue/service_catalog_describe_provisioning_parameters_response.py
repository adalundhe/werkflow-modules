from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_constraint_summary import ServiceCatalogConstraintSummary
from .service_catalog_provisioning_artifact_output import ServiceCatalogProvisioningArtifactOutput
from .service_catalog_provisioning_artifact_parameter import ServiceCatalogProvisioningArtifactParameter
from .service_catalog_provisioning_artifact_preferences import ServiceCatalogProvisioningArtifactPreferences
from .service_catalog_tag_option_summary import ServiceCatalogTagOptionSummary
from .service_catalog_usage_instruction import ServiceCatalogUsageInstruction


class ServiceCatalogDescribeProvisioningParametersResponse(BaseModel):
    ProvisioningArtifactParameters: list[ServiceCatalogProvisioningArtifactParameter] | None = None
    ConstraintSummaries: list[ServiceCatalogConstraintSummary] | None = None
    UsageInstructions: list[ServiceCatalogUsageInstruction] | None = None
    TagOptions: list[ServiceCatalogTagOptionSummary] | None = None
    ProvisioningArtifactPreferences: ServiceCatalogProvisioningArtifactPreferences | None = None
    ProvisioningArtifactOutputs: list[ServiceCatalogProvisioningArtifactOutput] | None = None
    ProvisioningArtifactOutputKeys: list[ServiceCatalogProvisioningArtifactOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
