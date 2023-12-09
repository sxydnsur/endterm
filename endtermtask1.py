import os

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.calculateGPA()
        self.setStatus()

    def calculateGPA(self):
        total_points = sum(score['score'] * score['credits'] for score in self.scores.values())
        total_credits = sum(score['credits'] for score in self.scores.values())
        self.overall_gpa = total_points / total_credits

    def setStatus(self):
        self.status = "Сдано" if self.overall_gpa >= 1.0 else "Не сдано"

    def showGPA(self):
        print(f"Средний балл студента {self.name}: {self.overall_gpa}")

    def showStatus(self):
        print(f"Статус студента {self.name}: {self.status}")

    def saveToFile(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"Имя: {self.name}\n")
            f.write("Оценки:\n")
            for course, score in self.scores.items():
                f.write(f"{course}: {score['score']} (Кредиты: {score['credits']})\n")
            f.write(f"Общий средний балл: {self.overall_gpa}\n")
            f.write(f"Статус: {self.status}\n")

   

   