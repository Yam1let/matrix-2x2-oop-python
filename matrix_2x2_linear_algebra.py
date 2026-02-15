"""
Matrix_2x2_linear_algebra
Author: Yam1let
"""

class Matrix2x2:
    """
    Represents a 2x2 matrix and supports
    determinant, multiplication, and inverse operations.
    """

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return f"{self.a} {self.b}\n{self.c} {self.d}"

    def determinant(self):
        return self.a * self.d - self.b * self.c

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix2x2(
                self.a * other,
                self.b * other,
                self.c * other,
                self.d * other
            )

        elif isinstance(other, Matrix2x2):
            return Matrix2x2(
                self.a * other.a + self.b * other.c,
                self.a * other.b + self.b * other.d,
                self.c * other.a + self.d * other.c,
                self.c * other.b + self.d * other.d
            )

        else:
            raise TypeError("Unsupported multiplication type")

    def __rmul__(self, other):
        return self * other

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")

        return (1 / det) * Matrix2x2(
            self.d,
            -self.b,
            -self.c,
            self.a
        )


if __name__ == "__main__":
    m1 = Matrix2x2(1, 2, 3, 4)
    print("Matrix:")
    print(m1)
    print("Determinant:", m1.determinant())
