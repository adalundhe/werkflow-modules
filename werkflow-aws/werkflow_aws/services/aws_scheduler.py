from werkflow_aws.models.scheduler import (
    SchedulerCreateScheduleGroupRequest,
    SchedulerCreateScheduleGroupResponse,
    SchedulerCreateScheduleRequest,
    SchedulerCreateScheduleResponse,
    SchedulerDeleteScheduleGroupRequest,
    SchedulerDeleteScheduleGroupResponse,
    SchedulerDeleteScheduleRequest,
    SchedulerDeleteScheduleResponse,
    SchedulerGetScheduleGroupRequest,
    SchedulerGetScheduleGroupResponse,
    SchedulerGetScheduleRequest,
    SchedulerGetScheduleResponse,
    SchedulerListScheduleGroupsRequest,
    SchedulerListScheduleGroupsResponse,
    SchedulerListSchedulesRequest,
    SchedulerListSchedulesResponse,
    SchedulerListTagsForResourceRequest,
    SchedulerListTagsForResourceResponse,
    SchedulerTagResourceRequest,
    SchedulerTagResourceResponse,
    SchedulerUntagResourceRequest,
    SchedulerUntagResourceResponse,
    SchedulerUpdateScheduleRequest,
    SchedulerUpdateScheduleResponse,
)
from werkflow_aws.types.scheduler_client import SchedulerClient
from .base import AWSBaseService


class AWSScheduler(AWSBaseService[SchedulerClient]):
    service_name = 'scheduler'
    boto3_service_name = 'scheduler'

    def __init__(self) -> None:
        super().__init__(service_name='scheduler', boto3_service_name='scheduler')

    async def create_schedule(
        self,
        request: SchedulerCreateScheduleRequest,
    ) -> SchedulerCreateScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_schedule, request, SchedulerCreateScheduleResponse)

    async def create_schedule_group(
        self,
        request: SchedulerCreateScheduleGroupRequest,
    ) -> SchedulerCreateScheduleGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_schedule_group, request, SchedulerCreateScheduleGroupResponse)

    async def delete_schedule(
        self,
        request: SchedulerDeleteScheduleRequest,
    ) -> SchedulerDeleteScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_schedule, request, SchedulerDeleteScheduleResponse)

    async def delete_schedule_group(
        self,
        request: SchedulerDeleteScheduleGroupRequest,
    ) -> SchedulerDeleteScheduleGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_schedule_group, request, SchedulerDeleteScheduleGroupResponse)

    async def get_schedule(
        self,
        request: SchedulerGetScheduleRequest,
    ) -> SchedulerGetScheduleResponse:
        client = self._require_client()
        return await self._execute(client.get_schedule, request, SchedulerGetScheduleResponse)

    async def get_schedule_group(
        self,
        request: SchedulerGetScheduleGroupRequest,
    ) -> SchedulerGetScheduleGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_schedule_group, request, SchedulerGetScheduleGroupResponse)

    async def list_schedule_groups(
        self,
        request: SchedulerListScheduleGroupsRequest | None = None,
    ) -> SchedulerListScheduleGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_schedule_groups, request, SchedulerListScheduleGroupsResponse)

    async def list_schedule_groups_paginated(
        self,
        request: SchedulerListScheduleGroupsRequest | None = None,
    ) -> list[SchedulerListScheduleGroupsResponse]:
        return await self._paginate('list_schedule_groups', request, SchedulerListScheduleGroupsResponse)

    async def list_schedules(
        self,
        request: SchedulerListSchedulesRequest | None = None,
    ) -> SchedulerListSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.list_schedules, request, SchedulerListSchedulesResponse)

    async def list_schedules_paginated(
        self,
        request: SchedulerListSchedulesRequest | None = None,
    ) -> list[SchedulerListSchedulesResponse]:
        return await self._paginate('list_schedules', request, SchedulerListSchedulesResponse)

    async def list_tags_for_resource(
        self,
        request: SchedulerListTagsForResourceRequest,
    ) -> SchedulerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SchedulerListTagsForResourceResponse)

    async def tag_resource(
        self,
        request: SchedulerTagResourceRequest,
    ) -> SchedulerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SchedulerTagResourceResponse)

    async def untag_resource(
        self,
        request: SchedulerUntagResourceRequest,
    ) -> SchedulerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SchedulerUntagResourceResponse)

    async def update_schedule(
        self,
        request: SchedulerUpdateScheduleRequest,
    ) -> SchedulerUpdateScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_schedule, request, SchedulerUpdateScheduleResponse)
