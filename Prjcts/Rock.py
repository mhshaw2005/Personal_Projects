import random

workouts= {
    "chest" : ["incline press", "flat press", "pec fly's", "dips", "push-ups"],
    "shoulders" :["overhead press", "lateral raises", "pike push-ups"],
    "arms" : ["bicep curls", "hammer curls", "triceps push down", "overhead triceps extension", "reverse curls", "wrist curls"],
    "legs" : ["hack squat", "split squats", "leg extensions", "leg curls", "hip abduction", "calf raises"],
    "back" : ["lat pull-downs","pull-ups", "rows", "rear delt fly", "shoulder shrugs"],
    "abs" : ["leg raises", "normal crunches", "decline crunches", "side plank", "plank"],
    "cardio" : ["treadmill running", "stairmaster", "rowing", "mountain climbers", "incline treadmill walking"]
}


class CurrSets:
    def __init__(self, sets, reps, weight, numWorkouts):
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.numWorkouts = numWorkouts


def _main():
    difficulty = input("On a scale of 1-10 pick your workout difficulty: ")
    diff_setting(int(difficulty))

    num = int(input("How many different areas do you want to work out, up to 7 (0 for random): "))
    if 0 < num < 8 :
        makesets(aresToWork(num))
    else:
        makesets(aresToWork(random.randint(1,7),True))


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


def aresToWork(num, rand = False):
    alpha = []
    prev = []

    if not rand:
        print("Options: Chest (1), Shoulders (2), Arms (3), Legs(4), Back (5), Abs(6), Cardio(7).")
        print("Please do not enter the same group twice!")

        for i in range(1,num + 1):
            temp = int(input("Enter the number of the desired area: "))
            if temp == 1:
                alpha.append("chest")
            elif temp == 2:
                alpha.append("shoulders")
            elif temp == 3:
                alpha.append("arms")
            elif temp == 4:
                alpha.append("legs")
            elif temp == 5:
                alpha.append("back")
            elif temp == 6:
                alpha.append("abs")
            elif temp == 7:
                alpha.append("cardio")
            prev.append(temp)
    elif rand:
        for i in range(1,num + 1):
            temp = random.randint(1,7)
            if temp == 1:
                alpha.append("chest")
            elif temp == 2:
                alpha.append("shoulders")
            elif temp == 3:
                alpha.append("arms")
            elif temp == 4:
                alpha.append("legs")
            elif temp == 5:
                alpha.append("back")
            elif temp == 6:
                alpha.append("abs")
            elif temp == 7:
                alpha.append("cardio")
            prev.append(temp)
    return alpha


def makesets(alpha):
    print("")


def randworkout(area):
    exercises = []

    theta = workouts.get(area)
    beta = random.choice(theta)
    exercises.append(beta)

    return  exercises

