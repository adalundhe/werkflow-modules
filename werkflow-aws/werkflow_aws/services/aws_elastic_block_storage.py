from werkflow_aws.models.ebs import (
    EBSCompleteSnapshotRequest,
    EBSCompleteSnapshotResponse,
    EBSGetSnapshotBlockRequest,
    EBSGetSnapshotBlockResponse,
    EBSListChangedBlocksRequest,
    EBSListChangedBlocksResponse,
    EBSListSnapshotBlocksRequest,
    EBSListSnapshotBlocksResponse,
    EBSPutSnapshotBlockRequest,
    EBSPutSnapshotBlockResponse,
    EBSStartSnapshotRequest,
    EBSStartSnapshotResponse,
)
from werkflow_aws.types.ebs_client import EBSClient
from .base import AWSBaseService


class AWSElasticBlockStorage(AWSBaseService[EBSClient]):
    service_name = 'ElasticBlockStorage'
    boto3_service_name = 'ebs'

    def __init__(self) -> None:
        super().__init__(
            service_name='ElasticBlockStorage',
            boto3_service_name='ebs',
        )

    async def list_snapshot_blocks(
        self,
        request: EBSListSnapshotBlocksRequest,
    ) -> EBSListSnapshotBlocksResponse:
        client = self._require_client()
        return await self._execute(
            client.list_snapshot_blocks,
            request,
            EBSListSnapshotBlocksResponse,
        )

    async def list_snapshot_blocks_paginated(
        self,
        request: EBSListSnapshotBlocksRequest,
    ) -> list[EBSListSnapshotBlocksResponse]:
        client = self._require_client()
        pages: list[EBSListSnapshotBlocksResponse] = []
        current_request = request
        while True:
            page = await self._execute(
                client.list_snapshot_blocks,
                current_request,
                EBSListSnapshotBlocksResponse,
            )
            pages.append(page)
            if not page.NextToken:
                break
            current_request = current_request.model_copy(
                update={'NextToken': page.NextToken},
            )
        return pages

    async def list_changed_blocks(
        self,
        request: EBSListChangedBlocksRequest,
    ) -> EBSListChangedBlocksResponse:
        client = self._require_client()
        return await self._execute(
            client.list_changed_blocks,
            request,
            EBSListChangedBlocksResponse,
        )

    async def list_changed_blocks_paginated(
        self,
        request: EBSListChangedBlocksRequest,
    ) -> list[EBSListChangedBlocksResponse]:
        client = self._require_client()
        pages: list[EBSListChangedBlocksResponse] = []
        current_request = request
        while True:
            page = await self._execute(
                client.list_changed_blocks,
                current_request,
                EBSListChangedBlocksResponse,
            )
            pages.append(page)
            if not page.NextToken:
                break
            current_request = current_request.model_copy(
                update={'NextToken': page.NextToken},
            )
        return pages

    async def get_snapshot_block(
        self,
        request: EBSGetSnapshotBlockRequest,
    ) -> EBSGetSnapshotBlockResponse:
        client = self._require_client()
        return await self._execute(
            client.get_snapshot_block,
            request,
            EBSGetSnapshotBlockResponse,
        )

    async def put_snapshot_block(
        self,
        request: EBSPutSnapshotBlockRequest,
    ) -> EBSPutSnapshotBlockResponse:
        client = self._require_client()
        return await self._execute(
            client.put_snapshot_block,
            request,
            EBSPutSnapshotBlockResponse,
        )

    async def start_snapshot(
        self,
        request: EBSStartSnapshotRequest,
    ) -> EBSStartSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.start_snapshot,
            request,
            EBSStartSnapshotResponse,
        )

    async def complete_snapshot(
        self,
        request: EBSCompleteSnapshotRequest,
    ) -> EBSCompleteSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.complete_snapshot,
            request,
            EBSCompleteSnapshotResponse,
        )
