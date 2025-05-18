def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Получает на вход словарь с интервалами и возвращает время общего присутствия
    ученика и учителя на уроке (в секундах).
    Под общим временем подразумевается одновременно присутствие обоих:
    ученика и учителя в рамках времени урока.
    """

    def merge_intervals(times: list[int]) -> list[tuple[int, int]]:
        """
        Преобразовывает лист тайм стемпов в интервалы формата [(12345, 12356), (..), ..].
        При необходимости производится слияние интервалов.
        """
        timestamp_tuples = [(times[i], times[i + 1]) for i in range(0, len(times), 2)]
        merged = []
        for start, end in sorted(timestamp_tuples):
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged

    def clip_intervals(
        merged_intervals: list[tuple[int, int]], lesson_start: int, lesson_end: int
    ) -> list[tuple[int, int]]:
        """
        Обрезать интервалы, чтобы они были в рамкак начала, конца урока.
        """
        ans = []
        for start, end in merged_intervals:
            if end > lesson_start and start < lesson_end:
                ans.append((max(start, lesson_start), min(end, lesson_end)))
        return ans

    def intersect_intervals(
        a: list[tuple[int, int]], b: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        """
        Найти пересечения в двух листах интервалов.
        """
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            start_a, end_a = a[i]
            start_b, end_b = b[j]
            start = max(start_a, start_b)
            end = min(end_a, end_b)
            if start < end:
                result.append((start, end))
            if end_a < end_b:
                i += 1
            else:
                j += 1
        return result

    lesson_start, lesson_end = intervals["lesson"]
    pupil_times = merge_intervals(intervals["pupil"])
    tutor_times = merge_intervals(intervals["tutor"])

    pupil_clipped = clip_intervals(pupil_times, lesson_start, lesson_end)
    tutor_clipped = clip_intervals(tutor_times, lesson_start, lesson_end)

    overlaps = intersect_intervals(pupil_clipped, tutor_clipped)

    total_time = sum(end - start for start, end in overlaps)
    return total_time


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
