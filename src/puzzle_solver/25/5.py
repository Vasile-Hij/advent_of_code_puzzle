title = "--- Day 5: Cafeteria ---"


class PuzzleSolver:
    @classmethod
    def sort_input(cls, puzzle_input):
        intervals, ids = [], []

        for row in puzzle_input:
            if row == "":
                continue
            if "-" in row:
                start, end = map(int, row.split("-"))
                intervals.append(range(start, end + 1))
            else:
                ids.append(int(row))

        ids.sort()
        intervals.sort(key=lambda r: r.start)

        return intervals, ids

    @classmethod
    def part_a(cls, puzzle_input):
        intervals, ids = cls.sort_input(puzzle_input)

        min_range_start = min(interval.start for interval in intervals)
        max_range_end = max(interval.stop for interval in intervals)

        possible_ids = [num for num in ids if min_range_start <= num <= max_range_end]

        matches = 0
        for number in possible_ids:
            for interval in intervals:
                if number < interval.start:
                    break
                if number in interval:
                    matches += 1
                    break
        return matches

    @classmethod
    def part_b(cls, puzzle_input):
        return
