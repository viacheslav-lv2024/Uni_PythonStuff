import math

class Rotate:
    def __init__(self, matrix: list[list[int]], degree: float, inplace=False):
        self.matrix = matrix
        self.degree = degree
        self.inplace = inplace

    def rotation(self) -> list[list[int]] or None:
        if self.degree not in [90, 180, -90]:
            raise ValueError("Rotation degree must be 90, 180, or -90.")

        n = len(self.matrix)
        center = (n - 1) / 2

        if self.inplace:
            rotated_matrix = self.matrix
        else:
            rotated_matrix = [row[:] for row in self.matrix]

        for i in range(n):
            for j in range(n):
                # Calculate relative position to the center
                x_rel, y_rel = i - center, j - center

                # Apply rotation matrix for each relative position
                if self.degree == 90:
                    new_x_rel = y_rel
                    new_y_rel = -x_rel
                elif self.degree == -90:
                    new_x_rel = -y_rel
                    new_y_rel = x_rel
                elif self.degree == 180:
                    new_x_rel = -x_rel
                    new_y_rel = -y_rel

                # Calculate new absolute position
                new_i = int(center + new_x_rel)
                new_j = int(center + new_y_rel)

                # Update the matrix
                rotated_matrix[new_i][new_j] = self.matrix[i][j]

        return rotated_matrix