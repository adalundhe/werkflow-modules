from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_error_details import AppStreamErrorDetails


class AppStreamExportImageTask(BaseModel):
    TaskId: StrictStr | None = None
    ImageArn: StrictStr | None = None
    AmiName: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    AmiDescription: StrictStr | None = None
    State: StrictStr | None = None
    AmiId: StrictStr | None = None
    TagSpecifications: dict[StrictStr, StrictStr] | None = None
    ErrorDetails: list[AppStreamErrorDetails] | None = None
