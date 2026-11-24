from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class EventBridgeClient(ABC):

    @abstractmethod
    def activate_event_source(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_replay(
        self,
        *,
        ReplayName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_api_destination(
        self,
        *,
        Name: str,
        ConnectionArn: str,
        InvocationEndpoint: str,
        HttpMethod: str,
        Description: str | None = None,
        InvocationRateLimitPerSecond: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_archive(
        self,
        *,
        ArchiveName: str,
        EventSourceArn: str,
        Description: str | None = None,
        EventPattern: str | None = None,
        RetentionDays: int | None = None,
        KmsKeyIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        Name: str,
        AuthorizationType: str,
        AuthParameters: dict[str, Any],
        Description: str | None = None,
        InvocationConnectivityParameters: dict[str, Any] | None = None,
        KmsKeyIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint(
        self,
        *,
        Name: str,
        RoutingConfig: dict[str, Any],
        EventBuses: list[dict[str, Any]],
        Description: str | None = None,
        ReplicationConfig: dict[str, Any] | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_bus(
        self,
        *,
        Name: str,
        EventSourceName: str | None = None,
        Description: str | None = None,
        KmsKeyIdentifier: str | None = None,
        DeadLetterConfig: dict[str, Any] | None = None,
        LogConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_partner_event_source(
        self,
        *,
        Name: str,
        Account: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_event_source(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deauthorize_connection(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_api_destination(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_archive(
        self,
        *,
        ArchiveName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_bus(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_partner_event_source(
        self,
        *,
        Name: str,
        Account: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rule(
        self,
        *,
        Name: str,
        EventBusName: str | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_api_destination(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_archive(
        self,
        *,
        ArchiveName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint(
        self,
        *,
        Name: str,
        HomeRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_bus(
        self,
        *,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_source(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_partner_event_source(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replay(
        self,
        *,
        ReplayName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_rule(
        self,
        *,
        Name: str,
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_rule(
        self,
        *,
        Name: str,
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_rule(
        self,
        *,
        Name: str,
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_api_destinations(
        self,
        *,
        NamePrefix: str | None = None,
        ConnectionArn: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_archives(
        self,
        *,
        NamePrefix: str | None = None,
        EventSourceArn: str | None = None,
        State: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connections(
        self,
        *,
        NamePrefix: str | None = None,
        ConnectionState: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_endpoints(
        self,
        *,
        NamePrefix: str | None = None,
        HomeRegion: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_buses(
        self,
        *,
        NamePrefix: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_sources(
        self,
        *,
        NamePrefix: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_partner_event_source_accounts(
        self,
        *,
        EventSourceName: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_partner_event_sources(
        self,
        *,
        NamePrefix: str,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_replays(
        self,
        *,
        NamePrefix: str | None = None,
        State: str | None = None,
        EventSourceArn: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rule_names_by_target(
        self,
        *,
        TargetArn: str,
        EventBusName: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rules(
        self,
        *,
        NamePrefix: str | None = None,
        EventBusName: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
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
    def list_targets_by_rule(
        self,
        *,
        Rule: str,
        EventBusName: str | None = None,
        NextToken: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_events(
        self,
        *,
        Entries: list[dict[str, Any]],
        EndpointId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_partner_events(
        self,
        *,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_permission(
        self,
        *,
        EventBusName: str | None = None,
        Action: str | None = None,
        Principal: str | None = None,
        StatementId: str | None = None,
        Condition: dict[str, Any] | None = None,
        Policy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_rule(
        self,
        *,
        Name: str,
        ScheduleExpression: str | None = None,
        EventPattern: str | None = None,
        State: str | None = None,
        Description: str | None = None,
        RoleArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_targets(
        self,
        *,
        Rule: str,
        Targets: list[dict[str, Any]],
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_permission(
        self,
        *,
        StatementId: str | None = None,
        RemoveAllPermissions: bool | None = None,
        EventBusName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_targets(
        self,
        *,
        Rule: str,
        Ids: list[str],
        EventBusName: str | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replay(
        self,
        *,
        ReplayName: str,
        EventSourceArn: str,
        EventStartTime: datetime.datetime | str,
        EventEndTime: datetime.datetime | str,
        Destination: dict[str, Any],
        Description: str | None = None,
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
    def test_event_pattern(
        self,
        *,
        EventPattern: str,
        Event: str,
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
    def update_api_destination(
        self,
        *,
        Name: str,
        Description: str | None = None,
        ConnectionArn: str | None = None,
        InvocationEndpoint: str | None = None,
        HttpMethod: str | None = None,
        InvocationRateLimitPerSecond: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_archive(
        self,
        *,
        ArchiveName: str,
        Description: str | None = None,
        EventPattern: str | None = None,
        RetentionDays: int | None = None,
        KmsKeyIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection(
        self,
        *,
        Name: str,
        Description: str | None = None,
        AuthorizationType: str | None = None,
        AuthParameters: dict[str, Any] | None = None,
        InvocationConnectivityParameters: dict[str, Any] | None = None,
        KmsKeyIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoint(
        self,
        *,
        Name: str,
        Description: str | None = None,
        RoutingConfig: dict[str, Any] | None = None,
        ReplicationConfig: dict[str, Any] | None = None,
        EventBuses: list[dict[str, Any]] | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_event_bus(
        self,
        *,
        Name: str | None = None,
        KmsKeyIdentifier: str | None = None,
        Description: str | None = None,
        DeadLetterConfig: dict[str, Any] | None = None,
        LogConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
