from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_segment_dimensions import PinpointSegmentDimensions
from .pinpoint_segment_group_list import PinpointSegmentGroupList
from .pinpoint_segment_import_resource import PinpointSegmentImportResource


class PinpointSegmentResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Dimensions: PinpointSegmentDimensions | None = None
    Id: StrictStr | None = None
    ImportDefinition: PinpointSegmentImportResource | None = None
    LastModifiedDate: StrictStr | None = None
    Name: StrictStr | None = None
    SegmentGroups: PinpointSegmentGroupList | None = None
    SegmentType: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    Version: StrictInt | None = None
