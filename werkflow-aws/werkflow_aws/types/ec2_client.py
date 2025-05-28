from __future__ import annotations
from botocore.paginate import Paginator
from abc import ABC, abstractmethod
from typing import Literal, Any


EC2Filters = Literal[
    "attachment.attach-time",
    "attachment.delete-on-termination",
    "attachment.device",
    "attachment.instance-id",
    "attachment.status",
    "availability-zone",
    "create-time",
    "encrypted",
    "fast-restored",
    "multi-attach-enabled",
    "operator.managed",
    "operator.principal",
    "size",
    "snapshot-id",
    "status",
    "tag",
    "tag-key",
    "volume-id",
    "volume-type"
]

Filter = dict[
    Literal['Name', 'Values'],
    EC2Filters | list[str]
]



class EC2Client(ABC):

    @abstractmethod
    def describe_volumes(
        self,
        VolumeIds: list[str] | None = None,
        DryRun: bool = False,
        Filters: list[Filter] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(
        self,
        Operation: str,
    ) -> Paginator:
        pass

    @abstractmethod
    def close(self):
        pass