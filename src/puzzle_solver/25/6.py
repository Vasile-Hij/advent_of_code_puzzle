title = "--- Day 6: Trash Compactor ---"


class PuzzleSolver:
    @classmethod
    def part_a(cls, puzzle_input):
        rows = [row.split() for row in puzzle_input if row.strip()]
        *value_rows, math_row = rows

        total = 0

        for *values, math_sign in zip(*value_rows, math_row):
            nums = list(map(int, values))
            total += cls.calculation(math_sign, nums)

        return total

    @classmethod
    def part_b(cls, puzzle_input):
        rows = [row for row in puzzle_input if row.strip()]
        longest_string = max(len(line) for line in rows)
        padded_lines = [row.ljust(longest_string) for row in rows]

        columns = list(zip(*padded_lines[:-1]))
        math_row = padded_lines[-1]

        total = 0
        column_index = len(columns) - 1

        while column_index >= 0:
            column = columns[column_index]
            if all(col == " " for col in column):
                column_index -= 1
                continue

            block_start = column_index
            while block_start >= 0 and not all(c == " " for c in columns[block_start]):
                block_start -= 1
            block_start_column = block_start + 1
            operator = math_row[block_start_column]

            nums = []
            current_col = column_index
            while current_col >= block_start_column:
                num_str = "".join(c for c in columns[current_col] if c != " ")
                if num_str:
                    nums.append(int(num_str))
                current_col -= 1

            calculation = cls.calculation(operator, nums)
            total += calculation

            column_index = block_start_column - 2

        return total

    @classmethod
    def calculation(cls, math_sign, nums):
        if math_sign == "+":
            return sum(nums)
        else:
            prod = 1
            for num in nums:
                prod *= num
            return prod
