from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .ec2_delete_snapshot_return_code import EC2DeleteSnapshotReturnCode


class EC2DeregisterImageResponse(BaseModel):
    Return: StrictBool | None = None
    DeleteSnapshotResults: list[EC2DeleteSnapshotReturnCode] | None = None
    ResponseMetadata: dict[str, Any] | None = None
