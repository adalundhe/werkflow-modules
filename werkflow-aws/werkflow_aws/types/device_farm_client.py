from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class DeviceFarmClient(ABC):

    @abstractmethod
    def create_device_pool(
        self,
        *,
        projectArn: str,
        name: str,
        rules: list[dict[str, Any]],
        description: str | None = None,
        maxDevices: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_profile(
        self,
        *,
        name: str,
        description: str | None = None,
        packageCleanup: bool | None = None,
        excludeAppPackagesFromCleanup: list[str] | None = None,
        rebootAfterUse: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_profile(
        self,
        *,
        projectArn: str,
        name: str,
        description: str | None = None,
        type: str | None = None,
        uplinkBandwidthBits: int | None = None,
        downlinkBandwidthBits: int | None = None,
        uplinkDelayMs: int | None = None,
        downlinkDelayMs: int | None = None,
        uplinkJitterMs: int | None = None,
        downlinkJitterMs: int | None = None,
        uplinkLossPercent: int | None = None,
        downlinkLossPercent: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        name: str,
        defaultJobTimeoutMinutes: int | None = None,
        vpcConfig: dict[str, Any] | None = None,
        environmentVariables: list[dict[str, Any]] | None = None,
        executionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_remote_access_session(
        self,
        *,
        projectArn: str,
        deviceArn: str,
        appArn: str | None = None,
        instanceArn: str | None = None,
        name: str | None = None,
        configuration: dict[str, Any] | None = None,
        interactionMode: str | None = None,
        skipAppResign: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_test_grid_project(
        self,
        *,
        name: str,
        description: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_test_grid_url(
        self,
        *,
        projectArn: str,
        expiresInSeconds: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_upload(
        self,
        *,
        projectArn: str,
        name: str,
        type: str,
        contentType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpce_configuration(
        self,
        *,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_device_pool(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_profile(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_profile(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_remote_access_session(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_run(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_test_grid_project(
        self,
        *,
        projectArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_upload(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpce_configuration(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_instance(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_pool(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_pool_compatibility(
        self,
        *,
        devicePoolArn: str,
        appArn: str | None = None,
        testType: str | None = None,
        test: dict[str, Any] | None = None,
        configuration: dict[str, Any] | None = None,
        projectArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_profile(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_profile(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_offering_status(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_remote_access_session(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_run(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_suite(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_test(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_test_grid_project(
        self,
        *,
        projectArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_test_grid_session(
        self,
        *,
        projectArn: str | None = None,
        sessionId: str | None = None,
        sessionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_upload(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpce_configuration(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def install_to_remote_access_session(
        self,
        *,
        remoteAccessSessionArn: str,
        appArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_artifacts(
        self,
        *,
        arn: str,
        type: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_device_instances(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_device_pools(
        self,
        *,
        arn: str,
        type: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_devices(
        self,
        *,
        arn: str | None = None,
        nextToken: str | None = None,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_profiles(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_network_profiles(
        self,
        *,
        arn: str,
        type: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_offering_promotions(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_offering_transactions(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_offerings(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        arn: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_remote_access_sessions(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_runs(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_samples(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_suites(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_grid_projects(
        self,
        *,
        maxResult: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_grid_session_actions(
        self,
        *,
        sessionArn: str,
        maxResult: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_grid_session_artifacts(
        self,
        *,
        sessionArn: str,
        type: str | None = None,
        maxResult: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_grid_sessions(
        self,
        *,
        projectArn: str,
        status: str | None = None,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        endTimeAfter: datetime.datetime | str | None = None,
        endTimeBefore: datetime.datetime | str | None = None,
        maxResult: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tests(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_unique_problems(
        self,
        *,
        arn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_uploads(
        self,
        *,
        arn: str,
        type: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpce_configurations(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_offering(
        self,
        *,
        offeringId: str,
        quantity: int,
        offeringPromotionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def renew_offering(
        self,
        *,
        offeringId: str,
        quantity: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def schedule_run(
        self,
        *,
        projectArn: str,
        test: dict[str, Any],
        appArn: str | None = None,
        devicePoolArn: str | None = None,
        deviceSelectionConfiguration: dict[str, Any] | None = None,
        name: str | None = None,
        configuration: dict[str, Any] | None = None,
        executionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_job(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_remote_access_session(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_run(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device_instance(
        self,
        *,
        arn: str,
        profileArn: str | None = None,
        labels: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device_pool(
        self,
        *,
        arn: str,
        name: str | None = None,
        description: str | None = None,
        rules: list[dict[str, Any]] | None = None,
        maxDevices: int | None = None,
        clearMaxDevices: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_instance_profile(
        self,
        *,
        arn: str,
        name: str | None = None,
        description: str | None = None,
        packageCleanup: bool | None = None,
        excludeAppPackagesFromCleanup: list[str] | None = None,
        rebootAfterUse: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_network_profile(
        self,
        *,
        arn: str,
        name: str | None = None,
        description: str | None = None,
        type: str | None = None,
        uplinkBandwidthBits: int | None = None,
        downlinkBandwidthBits: int | None = None,
        uplinkDelayMs: int | None = None,
        downlinkDelayMs: int | None = None,
        uplinkJitterMs: int | None = None,
        downlinkJitterMs: int | None = None,
        uplinkLossPercent: int | None = None,
        downlinkLossPercent: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        arn: str,
        name: str | None = None,
        defaultJobTimeoutMinutes: int | None = None,
        vpcConfig: dict[str, Any] | None = None,
        environmentVariables: list[dict[str, Any]] | None = None,
        executionRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_test_grid_project(
        self,
        *,
        projectArn: str,
        name: str | None = None,
        description: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_upload(
        self,
        *,
        arn: str,
        name: str | None = None,
        contentType: str | None = None,
        editContent: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpce_configuration(
        self,
        *,
        arn: str,
        vpceConfigurationName: str | None = None,
        vpceServiceName: str | None = None,
        serviceDnsName: str | None = None,
        vpceConfigurationDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
