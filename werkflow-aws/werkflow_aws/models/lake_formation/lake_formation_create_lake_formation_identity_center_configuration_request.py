from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_external_filtering_configuration import LakeFormationExternalFilteringConfiguration
from .lake_formation_service_integration_union import LakeFormationServiceIntegrationUnion


class LakeFormationCreateLakeFormationIdentityCenterConfigurationRequest(BaseModel):
    CatalogId: StrictStr | None = None
    InstanceArn: StrictStr | None = None
    ExternalFiltering: LakeFormationExternalFilteringConfiguration | None = None
    ShareRecipients: list[LakeFormationDataLakePrincipal] | None = None
    ServiceIntegrations: list[LakeFormationServiceIntegrationUnion] | None = None
