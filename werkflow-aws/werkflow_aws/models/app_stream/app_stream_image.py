from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_application import AppStreamApplication
from .app_stream_image_permissions import AppStreamImagePermissions
from .app_stream_image_software_metadata import AppStreamImageSoftwareMetadata
from .app_stream_image_state_change_reason import AppStreamImageStateChangeReason
from .app_stream_resource_error import AppStreamResourceError


class AppStreamImage(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    BaseImageArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    State: StrictStr | None = None
    Visibility: StrictStr | None = None
    ImageBuilderSupported: StrictBool | None = None
    ImageBuilderName: StrictStr | None = None
    Platform: StrictStr | None = None
    Description: StrictStr | None = None
    StateChangeReason: AppStreamImageStateChangeReason | None = None
    Applications: list[AppStreamApplication] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    PublicBaseImageReleasedDate: datetime.datetime | StrictStr | None = None
    AppstreamAgentVersion: StrictStr | None = None
    ImagePermissions: AppStreamImagePermissions | None = None
    ImageErrors: list[AppStreamResourceError] | None = None
    LatestAppstreamAgentVersion: StrictStr | None = None
    SupportedInstanceFamilies: list[StrictStr] | None = None
    DynamicAppProvidersEnabled: StrictStr | None = None
    ImageSharedWithOthers: StrictStr | None = None
    ManagedSoftwareIncluded: StrictBool | None = None
    ImageType: StrictStr | None = None
    ImageSoftwareMetadata: AppStreamImageSoftwareMetadata | None = None
