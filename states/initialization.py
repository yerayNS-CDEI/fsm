from state import State

class Initialization(State):
    def __init__(self, name):
        super().__init__(name)

    def on_enter(self, ctx):
        print(f"[{self.name}] Robot resting. Type 'start' to begin.")

    def run(self, ctx):
        if not ctx.get("start"):
            user_input = input(">> Order: ").strip().lower()
            if user_input == "start":
                ctx["start"] = True
                print(f"[{self.name}] Getting started...")
            else:
                print(f"[{self.name}] Unrecognized order.")
        else:
            print(f"[{self.name}] Order already received.")

    def check_transition(self, ctx):
        if ctx.get("start"):
            return "CreateMap"
        return None
