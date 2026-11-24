from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_external_filtering_configuration import LakeFormationExternalFilteringConfiguration
from .lake_formation_service_integration_union import LakeFormationServiceIntegrationUnion


class LakeFormationUpdateLakeFormationIdentityCenterConfigurationRequest(BaseModel):
    CatalogId: StrictStr | None = None
    ShareRecipients: list[LakeFormationDataLakePrincipal] | None = None
    ServiceIntegrations: list[LakeFormationServiceIntegrationUnion] | None = None
    ApplicationStatus: Literal['ENABLED', 'DISABLED'] | None = None
    ExternalFiltering: LakeFormationExternalFilteringConfiguration | None = None
