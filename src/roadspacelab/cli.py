"""Small command-line calculator for Road Space Lab boundary models."""
from __future__ import annotations

import argparse

from .capacity import (
    finite_length_change_gain,
    interpret_dynamic_area_claim,
    kmh_to_mps,
    length_capacity_elasticity_constant_gap,
    queue_slots_1d,
)
from .metrics import deadheading_multiplier


def _area_claim(args: argparse.Namespace) -> None:
    result = interpret_dynamic_area_claim(
        args.area_m2, args.width_m, kmh_to_mps(args.speed_kmh)
    )
    print(f"space_headway_m={result.space_headway_m:.3f}")
    print(f"time_headway_s={result.time_headway_s:.3f}")
    print(f"flow_vph_per_stream={result.flow_vph_per_stream:.1f}")


def _size_change(args: argparse.Namespace) -> None:
    speed = kmh_to_mps(args.speed_kmh)
    gain = finite_length_change_gain(
        speed, args.length_before_m, args.length_after_m, args.gap_m
    )
    elasticity = length_capacity_elasticity_constant_gap(
        args.length_before_m, args.gap_m
    )
    print(f"constant_gap_capacity_gain_pct={100 * gain:.3f}")
    print(f"local_length_elasticity={elasticity:.3f}")
    print(
        "fixed_time_headway_capacity_gain_pct=0.000 "
        "# when observed time headway itself is held fixed"
    )


def _queue(args: argparse.Namespace) -> None:
    print(
        queue_slots_1d(
            args.segment_length_m, args.vehicle_length_m, args.gap_m
        )
    )


def _deadhead(args: argparse.Namespace) -> None:
    print(f"vehicle_km_per_occupied_km={deadheading_multiplier(args.empty_share):.3f}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="roadspace",
        description="Transparent road-capacity boundary-model calculator",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    area = sub.add_parser("area-claim", help="reverse-engineer a dynamic m²/vehicle claim")
    area.add_argument("--area-m2", type=float, required=True)
    area.add_argument("--width-m", type=float, required=True)
    area.add_argument("--speed-kmh", type=float, required=True)
    area.set_defaults(func=_area_claim)

    size = sub.add_parser("size-change", help="test vehicle-length reduction under fixed-gap boundary model")
    size.add_argument("--length-before-m", type=float, required=True)
    size.add_argument("--length-after-m", type=float, required=True)
    size.add_argument("--gap-m", type=float, required=True)
    size.add_argument("--speed-kmh", type=float, required=True)
    size.set_defaults(func=_size_change)

    queue = sub.add_parser("queue", help="regular single-file stopped queue storage")
    queue.add_argument("--segment-length-m", type=float, required=True)
    queue.add_argument("--vehicle-length-m", type=float, required=True)
    queue.add_argument("--gap-m", type=float, required=True)
    queue.set_defaults(func=_queue)

    deadhead = sub.add_parser("deadhead", help="empty-VKT multiplier")
    deadhead.add_argument("--empty-share", type=float, required=True)
    deadhead.set_defaults(func=_deadhead)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
