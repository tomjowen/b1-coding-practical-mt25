class Control:
    def __init__(self):
        self.Kp = 0
        self.Kd = 0
    def get_action(self,observation,reference):
        return 