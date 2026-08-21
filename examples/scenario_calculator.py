"""Tiny transparent scenario; replace assumptions with measured values when possible."""
from roadspacelab.metrics import deadheading_multiplier, person_throughput, queue_storage, signal_capacity


def main() -> None:
    normal = queue_storage(100, 4.0, 0.8)
    shorter = queue_storage(100, 3.6, 0.8)
    capacity = signal_capacity(headway_s=1.9, green_s=45, cycle_s=90)
    print(f"100 m queue: 4.0 m cars={normal}, 3.6 m cars={shorter}")
    print(f"Signal baseline: {capacity:.0f} veh/h/lane")
    print(f"At 1.5 occupants: {person_throughput(capacity, 1.5):.0f} persons/h/lane")
    print(f"40% empty VKT: {deadheading_multiplier(.4):.3f} total km per occupied km")


if __name__ == "__main__":
    main()
