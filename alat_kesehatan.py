import time
import random

class Organ:
    def __init__(self, name):
        self.name = name
        self.status = "Normal"

    def work(self):
        # Simulasi kerja organ dengan kondisi acak
        if random.random() < 0.05:  # 5% kemungkinan gangguan
            self.status = "Gangguan"
        else:
            self.status = "Normal"
        return f"{self.name} bekerja: {self.status}"

class Body:
    def __init__(self):
        self.heart = Organ("Jantung")
        self.lungs = Organ("Paru-paru")
        self.brain = Organ("Otak")

    def simulate(self, duration=10):
        print("Simulasi tubuh dimulai...\n")
        for second in range(duration):
            print(f"Detik {second+1}:")
            print(self.heart.work())
            print(self.lungs.work())
            print(self.brain.work())
            print("-"*30)
            time.sleep(1)  # jeda 1 detik agar terasa realistis

if __name__ == "__main__":
    tubuh = Body()
    tubuh.simulate(duration=10)

