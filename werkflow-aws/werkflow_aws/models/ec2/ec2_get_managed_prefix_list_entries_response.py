from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_prefix_list_entry import EC2PrefixListEntry


class EC2GetManagedPrefixListEntriesResponse(BaseModel):
    Entries: list[EC2PrefixListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
