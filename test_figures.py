import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_unit_radius(self):
        """Проверяет площадь круга с радиусом 1 (должна равняться π)."""
        self.assertAlmostEqual(circle_area(1), math.pi)

    def test_perimeter_unit_radius(self):
        """Проверяет периметр круга с радиусом 1 (должен быть 2π)."""
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)

    def test_area_zero_radius(self):
        """Проверяет площадь круга с радиусом 0 (должна быть 0)."""
        self.assertEqual(circle_area(0), 0)

    def test_perimeter_zero_radius(self):
        """Проверяет периметр круга с радиусом 0 (должен быть 0)."""
        self.assertEqual(circle_perimeter(0), 0)

    def test_area_large_radius(self):
        """Проверяет площадь круга с большим радиусом (должна быть 1000^2 * π)."""
        self.assertAlmostEqual(circle_area(1000), 1000 ** 2 * math.pi)

    def test_perimeter_large_radius(self):
        """Проверяет периметр круга с большим радиусом (должен быть 2 * 1000 * π)."""
        self.assertAlmostEqual(circle_perimeter(1000), 2 * 1000 * math.pi)

    def test_area_negative_radius(self):
        """Проверяет, что возникает ошибка при вычислении площади с отрицательным радиусом."""
        with self.assertRaises(ValueError):
            circle_area(-5)

    def test_perimeter_negative_radius(self):
        """Проверяет, что возникает ошибка при вычислении периметра с отрицательным радиусом."""
        with self.assertRaises(ValueError):
            circle_perimeter(-5)

    def test_area_fractional_radius(self):
        """Проверяет площадь круга с дробным радиусом (должна быть 0.5^2 * π)."""
        self.assertAlmostEqual(circle_area(0.5), 0.5 ** 2 * math.pi)

    def test_perimeter_fractional_radius(self):
        """Проверяет периметр круга с дробным радиусом (должен быть 2 * 0.5 * π)."""
        self.assertAlmostEqual(circle_perimeter(0.5), 2 * 0.5 * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь прямоугольника (10, 5) (должна быть 50)."""
        self.assertEqual(rectangle_area(10, 5), 50)

    def test_perimeter(self):
        """Проверяет периметр прямоугольника (10, 5) (должен быть 30)."""
        self.assertEqual(rectangle_perimeter(10, 5), 30)

    def test_area_zero_width(self):
        """Проверяет площадь прямоугольника с шириной 0 (должна быть 0)."""
        self.assertEqual(rectangle_area(10, 0), 0)

    def test_perimeter_zero_width(self):
        """Проверяет периметр прямоугольника с шириной 0 (должен быть 20)."""
        self.assertEqual(rectangle_perimeter(10, 0), 20)

    def test_area_square(self):
        """Проверяет площадь квадратного прямоугольника (10, 10) (должна быть 100)."""
        self.assertEqual(rectangle_area(10, 10), 100)

    def test_perimeter_square(self):
        """Проверяет периметр квадратного прямоугольника (10, 10) (должен быть 40)."""
        self.assertEqual(rectangle_perimeter(10, 10), 40)

    def test_area_negative_side(self):
        """Проверяет, что возникает ошибка при вычислении площади с отрицательной стороной."""
        with self.assertRaises(ValueError):
            rectangle_area(-10, 5)

    def test_perimeter_negative_side(self):
        """Проверяет, что возникает ошибка при вычислении периметра с отрицательной стороной."""
        with self.assertRaises(ValueError):
            rectangle_perimeter(-10, 5)

    def test_area_large_sides(self):
        """Проверяет площадь большого прямоугольника (1000, 500) (должна быть 500000)."""
        self.assertEqual(rectangle_area(1000, 500), 500000)

    def test_perimeter_large_sides(self):
        """Проверяет периметр большого прямоугольника (1000, 500) (должен быть 3000)."""
        self.assertEqual(rectangle_perimeter(1000, 500), 3000)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь квадрата со стороной 10 (должна быть 100)."""
        self.assertEqual(square_area(10), 100)

    def test_perimeter(self):
        """Проверяет периметр квадрата со стороной 10 (должен быть 40)."""
        self.assertEqual(square_perimeter(10), 40)

    def test_area_zero_side(self):
        """Проверяет площадь квадрата со стороной 0 (должна быть 0)."""
        self.assertEqual(square_area(0), 0)

    def test_perimeter_zero_side(self):
        """Проверяет периметр квадрата со стороной 0 (должен быть 0)."""
        self.assertEqual(square_perimeter(0), 0)

    def test_area_large_side(self):
        """Проверяет площадь большого квадрата (1000) (должна быть 1000000)."""
        self.assertEqual(square_area(1000), 1000000)

    def test_perimeter_large_side(self):
        """Проверяет периметр большого квадрата (1000) (должен быть 4000)."""
        self.assertEqual(square_perimeter(1000), 4000)

    def test_area_negative_side(self):
        """Проверяет, что возникает ошибка при вычислении площади с отрицательной стороной."""
        with self.assertRaises(ValueError):
            square_area(-5)

    def test_perimeter_negative_side(self):
        """Проверяет, что возникает ошибка при вычислении периметра с отрицательной стороной."""
        with self.assertRaises(ValueError):
            square_perimeter(-5)

    def test_area_fractional_side(self):
        """Проверяет площадь квадрата с дробной стороной (0.5) (должна быть 0.25)."""
        self.assertEqual(square_area(0.5), 0.25)

    def test_perimeter_fractional_side(self):
        """Проверяет периметр квадрата с дробной стороной (0.5) (должен быть 2)."""
        self.assertEqual(square_perimeter(0.5), 2)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь треугольника (10, 5) (должна быть 25)."""
        self.assertEqual(triangle_area(10, 5), 25)

    def test_perimeter(self):
        """Проверяет периметр треугольника (3, 4, 5) (должен быть 12)."""
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_area_zero_base(self):
        """Проверяет площадь треугольника с основанием 0 (должна быть 0)."""
        self.assertEqual(triangle_area(0, 10), 0)

    def test_perimeter_zero_side(self):
        """Проверяет, периметр треугольника со стороной 0 (должно быть 0)."""
        self.assertEqual(triangle_perimeter(0, 5, 7), 12)

    def test_area_negative_base(self):
        """Проверяет, что возникает ошибка при вычислении площади с отрицательным основанием."""
        with self.assertRaises(ValueError):
            triangle_area(-10, 5)

    def test_perimeter_negative_side(self):
        """Проверяет, что возникает ошибка при вычислении периметра с отрицательной стороной."""
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 4, 5)

    def test_area_fractional_height(self):
        """Проверяет площадь треугольника с дробной высотой (0.5) (должна быть 2.5)."""
        self.assertEqual(triangle_area(10, 0.5), 2.5)

    def test_perimeter_fractional_sides(self):
        """Проверяет периметр треугольника с дробными сторонами (1.5, 2.5, 3.5) (должен быть 7.5)."""
        self.assertEqual(triangle_perimeter(1.5, 2.5, 3.5), 7.5)

    def test_area_large_base_and_height(self):
        """Проверяет площадь большого треугольника (1000, 500) (должна быть 250000)."""
        self.assertEqual(triangle_area(1000, 500), 250000)

    def test_perimeter_large_sides(self):
        """Проверяет периметр большого треугольника (1000, 500, 300) (должен быть 1800)."""
        self.assertEqual(triangle_perimeter(1000, 500, 300), 1800)


if __name__ == '__main__':
    unittest.main()
