from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .work_spaces_custom_workspace_image_import_error_details import WorkSpacesCustomWorkspaceImageImportErrorDetails
from .work_spaces_image_source_identifier import WorkSpacesImageSourceIdentifier


class WorkSpacesDescribeCustomWorkspaceImageImportResponse(BaseModel):
    ImageId: StrictStr | None = None
    InfrastructureConfigurationArn: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    ProgressPercentage: StrictInt | None = None
    Created: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ImageSource: WorkSpacesImageSourceIdentifier | None = None
    ImageBuilderInstanceId: StrictStr | None = None
    ErrorDetails: list[WorkSpacesCustomWorkspaceImageImportErrorDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
