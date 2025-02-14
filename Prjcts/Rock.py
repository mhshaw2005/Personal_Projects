chest = ["incline press", "flat press", "pec fly's", "dips", "push-ups"]
shoulders = ["overhead press", "lateral raises", "pike push-ups"]
arms = ["bicep curls", "hammer curls", "triceps push down", "overhead triceps extension", "reverse curls", "wrist curls"]
legs = ["hack squat", "split squats", "leg extensions", "leg curls", "hip abduction", "calf raises"]
back = ["lat pull-downs","pull-ups", "rows", "rear delt fly", "shoulder shrugs"]
abs = ["leg raises", "normal crunches", "decline crunches", "side plank", "plank"]
cardio = ["treadmill running", "stairmaster", "rowing", "mountain climbers", "incline treadmill walking"]


class CurrSets:
    def __init__(self, sets, reps, weight, numWorkouts):
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.numWorkouts = numWorkouts


def _main():
    difficulty = input("On a scale of 1-10 pick your workout difficulty: ")
    diff_setting(int(difficulty))


def diff_setting(difficulty):
    if difficulty == 1:
        diff = CurrSets(2,5, "light", 5)
    elif difficulty == 2:
        diff = CurrSets(2,5, "light", 6)
    elif difficulty == 3:
        diff = CurrSets(3,8, "light", 5)
    elif difficulty == 4:
        diff = CurrSets(3,8, "light", 6)
    elif difficulty == 5:
        diff = CurrSets(3,8, "medium", 6)
    elif difficulty == 6:
        diff = CurrSets(3,8, "medium", 8)
    elif difficulty == 7:
        diff = CurrSets(3,10, "medium", 8)
    elif difficulty == 8:
        diff = CurrSets(3,10, "heavy", 8)
    elif difficulty == 9:
        diff = CurrSets(2,12, "heavy", 8)
    elif difficulty == 10:
        diff = CurrSets(3,12, "heavy", 8)
    else:
        print("Not a valid level. Try again!")
        _main()

def aresToWork():
