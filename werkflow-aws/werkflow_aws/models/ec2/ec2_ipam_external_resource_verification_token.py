from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamExternalResourceVerificationToken(BaseModel):
    IpamExternalResourceVerificationTokenId: StrictStr | None = None
    IpamExternalResourceVerificationTokenArn: StrictStr | None = None
    IpamId: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    TokenValue: StrictStr | None = None
    TokenName: StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    State: StrictStr | None = None
