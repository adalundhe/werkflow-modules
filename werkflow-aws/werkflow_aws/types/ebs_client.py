from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, BinaryIO

from botocore.paginate import Paginator


class EBSClient(ABC):

    @abstractmethod
    def list_snapshot_blocks(
        self,
        SnapshotId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StartingBlockIndex: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_changed_blocks(
        self,
        SecondSnapshotId: str,
        FirstSnapshotId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StartingBlockIndex: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_snapshot_block(
        self,
        SnapshotId: str,
        BlockIndex: int,
        BlockToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_snapshot_block(
        self,
        SnapshotId: str,
        BlockIndex: int,
        BlockData: bytes | BinaryIO,
        DataLength: int,
        Checksum: str,
        ChecksumAlgorithm: str,
        Progress: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_snapshot(
        self,
        VolumeSize: int,
        ParentSnapshotId: str | None = None,
        Tags: list[dict[str, str]] | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyArn: str | None = None,
        Timeout: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_snapshot(
        self,
        SnapshotId: str,
        ChangedBlocksCount: int,
        Checksum: str | None = None,
        ChecksumAlgorithm: str | None = None,
        ChecksumAggregationMethod: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
