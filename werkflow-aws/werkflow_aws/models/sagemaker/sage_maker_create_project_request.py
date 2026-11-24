from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_create_template_provider import SageMakerCreateTemplateProvider
from .sage_maker_service_catalog_provisioning_details import SageMakerServiceCatalogProvisioningDetails
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateProjectRequest(BaseModel):
    ProjectName: StrictStr
    ProjectDescription: StrictStr | None = None
    ServiceCatalogProvisioningDetails: SageMakerServiceCatalogProvisioningDetails | None = None
    Tags: list[SageMakerTagModel] | None = None
    TemplateProviders: list[SageMakerCreateTemplateProvider] | None = None
