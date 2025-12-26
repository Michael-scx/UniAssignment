




def process_fitness_data(filename):
    activity_totals = {}
    iron_athletes = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 4:
                continue

            name, activity, cardio, strength = parts

            try:
                cardio_minutes = int(cardio)
                strength_minutes = int(strength)
            except ValueError:
                continue

            total_minutes = cardio_minutes + strength_minutes

            activity_totals[activity] = activity_totals.get(activity, 0) + total_minutes

            if total_minutes > 90:
                iron_athletes.append((name, total_minutes))

    return activity_totals, iron_athletes

def save_fitness_report(activity_totals, elite_athletes):
    with open("fitness_report.txt", "w") as file:
        file.write("ACTIVITY TYPE TOTALS (Minutes)\n")
        file.write("--------------------------------\n")

        for activity in ["Yoga", "Crossfit", "Running"]:
            if activity in activity_totals:
                file.write(f"{activity}: {activity_totals[activity]}\n")

        file.write("\nIRON ATHLETES (> 90 mins)\n")
        file.write("-------------------------\n")

        
        for name in ["Mike", "Emily", "Chris"]:
            for athlete, minutes in elite_athletes:
                if athlete == name:
                    file.write(f"{athlete} ({minutes} mins)\n")


activity_totals, iron_athletes = process_fitness_data("workout_log.txt")
save_fitness_report(activity_totals, iron_athletes)

with open("fitness_report.txt","r") as f:
    print(f.read())





