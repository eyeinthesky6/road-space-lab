"""Adapter for the published SPT Chennai trajectory schema.

SPT source: https://www.chennaitrafficdata.com/
Citation: Rajput et al. (2026), Transportation Research Part C 182, 105431.

This module does not download or redistribute SPT. Give it a locally obtained CSV
that you are permitted to use.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, TextIO

SPT_CLASS = {
    0: "two_wheeler",
    1: "car",
    2: "three_wheeler",
    3: "light_commercial_vehicle",
    4: "heavy_commercial_vehicle",
}

_REQUIRED = {
    "New_TimeStamp",
    "Vehicle_ID",
    "Vehicle_class",
    "Length",
    "Width",
    "Long_smooth",
    "v_smooth",
    "a_smooth",
    "Latright_smooth",
    "vy_smooth",
    "ay_smooth",
}


@dataclass(frozen=True, slots=True)
class TrajectoryPoint:
    dataset: str
    vehicle_id: str
    vehicle_class: str
    timestamp_s: float
    x_m: float
    y_m: float
    length_m: float
    width_m: float
    speed_mps: float
    accel_long_mps2: float
    velocity_lat_mps: float
    accel_lat_mps2: float


def _reader(source: str | Path | TextIO) -> tuple[csv.DictReader, TextIO | None]:
    if hasattr(source, "read"):
        return csv.DictReader(source), None  # type: ignore[arg-type]
    handle = Path(source).open("r", newline="", encoding="utf-8-sig")
    return csv.DictReader(handle), handle


def iter_spt(source: str | Path | TextIO) -> Iterator[TrajectoryPoint]:
    """Yield SPT rows normalized into Road Space Lab's canonical point schema."""
    reader, owned_handle = _reader(source)
    try:
        fields = set(reader.fieldnames or [])
        missing = _REQUIRED - fields
        if missing:
            raise ValueError(f"SPT CSV missing required columns: {sorted(missing)}")

        for row_number, row in enumerate(reader, start=2):
            try:
                class_id = int(row["Vehicle_class"])
                vehicle_class = SPT_CLASS.get(class_id, f"unknown_{class_id}")
                yield TrajectoryPoint(
                    dataset="SPT-Chennai",
                    vehicle_id=str(row["Vehicle_ID"]),
                    vehicle_class=vehicle_class,
                    timestamp_s=float(row["New_TimeStamp"]),
                    x_m=float(row["Long_smooth"]),
                    y_m=float(row["Latright_smooth"]),
                    length_m=float(row["Length"]),
                    width_m=float(row["Width"]),
                    speed_mps=float(row["v_smooth"]),
                    accel_long_mps2=float(row["a_smooth"]),
                    velocity_lat_mps=float(row["vy_smooth"]),
                    accel_lat_mps2=float(row["ay_smooth"]),
                )
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid SPT value at CSV row {row_number}: {exc}") from exc
    finally:
        if owned_handle is not None:
            owned_handle.close()


def group_by_vehicle(points: Iterable[TrajectoryPoint]) -> dict[str, list[TrajectoryPoint]]:
    """Group canonical points by vehicle ID and sort each trajectory by time."""
    grouped: dict[str, list[TrajectoryPoint]] = {}
    for point in points:
        grouped.setdefault(point.vehicle_id, []).append(point)
    for trajectory in grouped.values():
        trajectory.sort(key=lambda p: p.timestamp_s)
    return grouped
