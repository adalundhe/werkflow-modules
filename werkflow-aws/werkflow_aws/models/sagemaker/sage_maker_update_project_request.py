from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_service_catalog_provisioning_update_details import SageMakerServiceCatalogProvisioningUpdateDetails
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_update_template_provider import SageMakerUpdateTemplateProvider


class SageMakerUpdateProjectRequest(BaseModel):
    ProjectName: StrictStr
    ProjectDescription: StrictStr | None = None
    ServiceCatalogProvisioningUpdateDetails: SageMakerServiceCatalogProvisioningUpdateDetails | None = None
    Tags: list[SageMakerTagModel] | None = None
    TemplateProvidersToUpdate: list[SageMakerUpdateTemplateProvider] | None = None
