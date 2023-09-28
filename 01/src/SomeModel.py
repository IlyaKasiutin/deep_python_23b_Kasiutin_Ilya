import random


class SomeModel:
    def predict(self, message: str) -> float:
        return random.random()


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if bad_thresholds < 0.0 or good_thresholds > 1.0 or bad_thresholds >= good_thresholds:
        raise ValueError("bad_thresholds must be in [0, 1), good_thresholds must be in (0, 1], "
                         "also bad_thresholds < good_thresholds")

    if type(message) != str:
        raise TypeError("message must be str")

    res = model.predict(message)

    if type(res) != float:
        raise TypeError("model.predict(message) must return float value in range [0, 1]")

    if res < bad_thresholds:
        return "неуд"
    elif bad_thresholds <= res < good_thresholds:
        return "норм"
    else:
        return "отл"
