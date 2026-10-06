DIFFICULTIES = {
    "beginner": {
        "rows": 9,
        "cols": 9,
        "mines": 10
    },
    "intermediate": {
        "rows": 16,
        "cols": 16,
        "mines": 40
    },
    "expert": {
        "rows": 16,
        "cols": 30,
        "mines": 99
    }
}


def get_difficulty(name):
    if name not in DIFFICULTIES:
        raise ValueError(f"Unknown difficulty: {name}")

    return DIFFICULTIES[name]