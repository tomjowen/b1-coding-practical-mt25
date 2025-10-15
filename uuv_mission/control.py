class Control:
    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
        self.prev = 0
        self.error = 0
        self.action = 0
    def get_action(self, observation, reference):
        self.error = reference - observation
        self.action = self.Kp * self.error + self.Kd * (self.error - self.prev)
        self.prev = self.error
        return self.action
