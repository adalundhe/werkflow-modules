from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_service_catalog_provisioned_product_details import SageMakerServiceCatalogProvisionedProductDetails
from .sage_maker_service_catalog_provisioning_details import SageMakerServiceCatalogProvisioningDetails
from .sage_maker_template_provider_detail import SageMakerTemplateProviderDetail
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeProjectResponse(BaseModel):
    ProjectArn: StrictStr | None = None
    ProjectName: StrictStr | None = None
    ProjectId: StrictStr | None = None
    ProjectDescription: StrictStr | None = None
    ServiceCatalogProvisioningDetails: SageMakerServiceCatalogProvisioningDetails | None = None
    ServiceCatalogProvisionedProductDetails: SageMakerServiceCatalogProvisionedProductDetails | None = None
    ProjectStatus: StrictStr | None = None
    TemplateProviderDetails: list[SageMakerTemplateProviderDetail] | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
