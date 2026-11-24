from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_content_dependency import SageMakerHubContentDependency
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeHubContentResponse(BaseModel):
    HubContentName: StrictStr | None = None
    HubContentArn: StrictStr | None = None
    HubContentVersion: StrictStr | None = None
    HubContentType: StrictStr | None = None
    DocumentSchemaVersion: StrictStr | None = None
    HubName: StrictStr | None = None
    HubArn: StrictStr | None = None
    HubContentDisplayName: StrictStr | None = None
    HubContentDescription: StrictStr | None = None
    HubContentMarkdown: StrictStr | None = None
    HubContentDocument: StrictStr | None = None
    SageMakerPublicHubContentArn: StrictStr | None = None
    ReferenceMinVersion: StrictStr | None = None
    SupportStatus: StrictStr | None = None
    HubContentSearchKeywords: list[StrictStr] | None = None
    HubContentDependencies: list[SageMakerHubContentDependency] | None = None
    HubContentStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
