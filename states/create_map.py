from state import State

class CreateMap(State):
    def __init__(self, name):
        super().__init__(name)
        self.started = False        # internal flag
        self.step_count = 0
        self.MAX_STEPS = 5

    def on_enter(self, ctx):
        print(f"Advancing to state [{self.name}].")
        self.started = False
        self.step_count = 0
        ctx["map_ready"] = False
        ctx["error_triggered"] = False

    def run(self, ctx):
        if self.step_count >= self.MAX_STEPS:
            if not ctx.get("error_triggered"):
                print(f"[{self.name}] ERROR: The maximum time was exceeded.")
                ctx["error_triggered"] = True
            return

        if not self.started:
            print(f"[{self.name}] Starting map creation...")
            self.started = True

            # service call to create the map
            if not ctx["map_ready"]:
                user_input = input(">> Finished map? ").strip().lower()
                if user_input == "yes":
                    ctx["map_ready"] = True
                    print(f"[{self.name}] Map creation completed.")

        else:
            print(f"[{self.name}] Supervising map creation. Step {self.step_count + 1}...")
            self.step_count += 1
        
            if not ctx["map_ready"]:
                user_input = input(">> Finished map? ").strip().lower()
                if user_input == "yes":
                    ctx["map_ready"] = True
                    print(f"[{self.name}] Map creation completed.")

    def check_transition(self, ctx):
        if ctx.get("map_ready"):
            return "ComputeWallPoints"
        if ctx.get("error_triggered"):
            return "Error"
        return None
