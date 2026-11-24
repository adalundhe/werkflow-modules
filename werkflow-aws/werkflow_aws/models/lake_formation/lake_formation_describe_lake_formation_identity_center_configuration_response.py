from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_external_filtering_configuration import LakeFormationExternalFilteringConfiguration
from .lake_formation_service_integration_union import LakeFormationServiceIntegrationUnion


class LakeFormationDescribeLakeFormationIdentityCenterConfigurationResponse(BaseModel):
    CatalogId: StrictStr | None = None
    InstanceArn: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
    ExternalFiltering: LakeFormationExternalFilteringConfiguration | None = None
    ShareRecipients: list[LakeFormationDataLakePrincipal] | None = None
    ServiceIntegrations: list[LakeFormationServiceIntegrationUnion] | None = None
    ResourceShare: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
