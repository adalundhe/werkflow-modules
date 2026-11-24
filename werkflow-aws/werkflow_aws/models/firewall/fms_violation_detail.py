from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_resource_violation import FMSResourceViolation
from .fms_tag import FMSTag


class FMSViolationDetail(BaseModel):
    PolicyId: StrictStr | None = None
    MemberAccount: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceViolations: list[FMSResourceViolation] | None = None
    ResourceTags: list[FMSTag] | None = None
    ResourceDescription: StrictStr | None = None
