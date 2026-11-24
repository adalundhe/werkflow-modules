from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class LocationClient(ABC):

    @abstractmethod
    def associate_tracker_consumer(
        self,
        *,
        TrackerName: str,
        ConsumerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_device_position_history(
        self,
        *,
        TrackerName: str,
        DeviceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_geofence(
        self,
        *,
        CollectionName: str,
        GeofenceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_evaluate_geofences(
        self,
        *,
        CollectionName: str,
        DevicePositionUpdates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_device_position(
        self,
        *,
        TrackerName: str,
        DeviceIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_geofence(
        self,
        *,
        CollectionName: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_device_position(
        self,
        *,
        TrackerName: str,
        Updates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def calculate_route(
        self,
        *,
        CalculatorName: str,
        DeparturePosition: list[float | int],
        DestinationPosition: list[float | int],
        WaypointPositions: list[list[float | int]] | None = None,
        TravelMode: str | None = None,
        DepartureTime: datetime.datetime | str | None = None,
        DepartNow: bool | None = None,
        DistanceUnit: str | None = None,
        IncludeLegGeometry: bool | None = None,
        CarModeOptions: dict[str, Any] | None = None,
        TruckModeOptions: dict[str, Any] | None = None,
        ArrivalTime: datetime.datetime | str | None = None,
        OptimizeFor: str | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def calculate_route_matrix(
        self,
        *,
        CalculatorName: str,
        DeparturePositions: list[list[float | int]],
        DestinationPositions: list[list[float | int]],
        TravelMode: str | None = None,
        DepartureTime: datetime.datetime | str | None = None,
        DepartNow: bool | None = None,
        DistanceUnit: str | None = None,
        CarModeOptions: dict[str, Any] | None = None,
        TruckModeOptions: dict[str, Any] | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_geofence_collection(
        self,
        *,
        CollectionName: str,
        PricingPlan: str | None = None,
        PricingPlanDataSource: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key(
        self,
        *,
        KeyName: str,
        Restrictions: dict[str, Any],
        Description: str | None = None,
        ExpireTime: datetime.datetime | str | None = None,
        NoExpiry: bool | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_map(
        self,
        *,
        MapName: str,
        Configuration: dict[str, Any],
        PricingPlan: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_place_index(
        self,
        *,
        IndexName: str,
        DataSource: str,
        PricingPlan: str | None = None,
        Description: str | None = None,
        DataSourceConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_calculator(
        self,
        *,
        CalculatorName: str,
        DataSource: str,
        PricingPlan: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tracker(
        self,
        *,
        TrackerName: str,
        PricingPlan: str | None = None,
        KmsKeyId: str | None = None,
        PricingPlanDataSource: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        PositionFiltering: str | None = None,
        EventBridgeEnabled: bool | None = None,
        KmsKeyEnableGeospatialQueries: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_geofence_collection(
        self,
        *,
        CollectionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key(
        self,
        *,
        KeyName: str,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_map(
        self,
        *,
        MapName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_place_index(
        self,
        *,
        IndexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_calculator(
        self,
        *,
        CalculatorName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tracker(
        self,
        *,
        TrackerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_geofence_collection(
        self,
        *,
        CollectionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key(
        self,
        *,
        KeyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_map(
        self,
        *,
        MapName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_place_index(
        self,
        *,
        IndexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_route_calculator(
        self,
        *,
        CalculatorName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tracker(
        self,
        *,
        TrackerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_tracker_consumer(
        self,
        *,
        TrackerName: str,
        ConsumerArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def forecast_geofence_events(
        self,
        *,
        CollectionName: str,
        DeviceState: dict[str, Any],
        TimeHorizonMinutes: float | int | None = None,
        DistanceUnit: str | None = None,
        SpeedUnit: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_position(
        self,
        *,
        TrackerName: str,
        DeviceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_position_history(
        self,
        *,
        TrackerName: str,
        DeviceId: str,
        NextToken: str | None = None,
        StartTimeInclusive: datetime.datetime | str | None = None,
        EndTimeExclusive: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_geofence(
        self,
        *,
        CollectionName: str,
        GeofenceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_map_glyphs(
        self,
        *,
        MapName: str,
        FontStack: str,
        FontUnicodeRange: str,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_map_sprites(
        self,
        *,
        MapName: str,
        FileName: str,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_map_style_descriptor(
        self,
        *,
        MapName: str,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_map_tile(
        self,
        *,
        MapName: str,
        Z: str,
        X: str,
        Y: str,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_place(
        self,
        *,
        IndexName: str,
        PlaceId: str,
        Language: str | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_device_positions(
        self,
        *,
        TrackerName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        FilterGeometry: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_geofence_collections(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_geofences(
        self,
        *,
        CollectionName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_keys(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_maps(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_place_indexes(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_route_calculators(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tracker_consumers(
        self,
        *,
        TrackerName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trackers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_geofence(
        self,
        *,
        CollectionName: str,
        GeofenceId: str,
        Geometry: dict[str, Any],
        GeofenceProperties: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_place_index_for_position(
        self,
        *,
        IndexName: str,
        Position: list[float | int],
        MaxResults: int | None = None,
        Language: str | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_place_index_for_suggestions(
        self,
        *,
        IndexName: str,
        Text: str,
        BiasPosition: list[float | int] | None = None,
        FilterBBox: list[float | int] | None = None,
        FilterCountries: list[str] | None = None,
        MaxResults: int | None = None,
        Language: str | None = None,
        FilterCategories: list[str] | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_place_index_for_text(
        self,
        *,
        IndexName: str,
        Text: str,
        BiasPosition: list[float | int] | None = None,
        FilterBBox: list[float | int] | None = None,
        FilterCountries: list[str] | None = None,
        MaxResults: int | None = None,
        Language: str | None = None,
        FilterCategories: list[str] | None = None,
        Key: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_job(
        self,
        *,
        Action: str,
        ExecutionRoleArn: str,
        InputOptions: dict[str, Any],
        OutputOptions: dict[str, Any],
        ClientToken: str | None = None,
        ActionOptions: dict[str, Any] | None = None,
        Name: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_geofence_collection(
        self,
        *,
        CollectionName: str,
        PricingPlan: str | None = None,
        PricingPlanDataSource: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_key(
        self,
        *,
        KeyName: str,
        Description: str | None = None,
        ExpireTime: datetime.datetime | str | None = None,
        NoExpiry: bool | None = None,
        ForceUpdate: bool | None = None,
        Restrictions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_map(
        self,
        *,
        MapName: str,
        PricingPlan: str | None = None,
        Description: str | None = None,
        ConfigurationUpdate: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_place_index(
        self,
        *,
        IndexName: str,
        PricingPlan: str | None = None,
        Description: str | None = None,
        DataSourceConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_route_calculator(
        self,
        *,
        CalculatorName: str,
        PricingPlan: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_tracker(
        self,
        *,
        TrackerName: str,
        PricingPlan: str | None = None,
        PricingPlanDataSource: str | None = None,
        Description: str | None = None,
        PositionFiltering: str | None = None,
        EventBridgeEnabled: bool | None = None,
        KmsKeyEnableGeospatialQueries: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_device_position(
        self,
        *,
        TrackerName: str,
        DeviceState: dict[str, Any],
        DistanceUnit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
