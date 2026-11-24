from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerDescribeImageVersionResponse(BaseModel):
    BaseImage: StrictStr | None = None
    ContainerImage: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ImageArn: StrictStr | None = None
    ImageVersionArn: StrictStr | None = None
    ImageVersionStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    VendorGuidance: StrictStr | None = None
    JobType: StrictStr | None = None
    MLFramework: StrictStr | None = None
    ProgrammingLang: StrictStr | None = None
    Processor: StrictStr | None = None
    Horovod: StrictBool | None = None
    ReleaseNotes: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
