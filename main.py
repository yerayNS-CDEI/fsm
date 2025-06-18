from machine import StateMachine
from states import Initialization, CreateMap, ComputeWallPoints, WallTargetSelection, NavigateToTarget, ScanWall, HomePosition, Finished, Error
# Estado del sistema simulado
context = {
    "start": False,
    "map_ready": False,
    "map_in_progress": False,
    "database_generated": False,
    "target_selected": False,
    "walls_left": 3,
    "scan_done": False,
    "fatal": False,
    "error_triggered": False,
    "home": False,
    "finished": False,
}

# Crear estados
states = [
    Initialization("Initialization"),
    CreateMap("CreateMap"),
    ComputeWallPoints("ComputeWallPoints"),
    WallTargetSelection("WallTargetSelection"),
    NavigateToTarget("NavigateToTarget"),
    ScanWall("ScanWall"),
    HomePosition("HomePosition"),
    Finished("Finished"),
    Error("Error"),
]

# Máquina de estados
machine = StateMachine(states, "Initialization", context)

# Ejecutar pasos manualmente
for step in range(100):
    print(f"\n--- Step {step} ---")
    machine.step()
    if context.get("finished") or context.get("error_triggered"):
        print("System terminated")
        break
