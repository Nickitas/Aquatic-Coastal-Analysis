import math
from typing import Tuple, List
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon


class GeoUtils:
    """ Этот модуль содержит утилитарные функции для работы с географическими и картографическими данными, включая расчёты, преобразования и обработку координат. """
    @staticmethod
    def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """
        Рассчитывает расстояние между двумя точками на поверхности Земли
        с использованием формулы гаверсинуса.

        :param coord1: Координаты первой точки (широта, долгота) в градусах.
        :param coord2: Координаты второй точки (широта, долгота) в градусах.
        :return: Расстояние между точками в километрах.
        """
        R = 6371  # Радиус Земли в километрах
        lat1, lon1 = map(math.radians, coord1)
        lat2, lon2 = map(math.radians, coord2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    @staticmethod
    def calculate_coastline_length(geometry: LineString) -> float:
        """
        Рассчитывает длину береговой линии.

        :param geometry: LineString, представляющий береговую линию.
        :return: Длина береговой линии в километрах.
        """
        if not isinstance(geometry, LineString):
            raise ValueError("Геометрия должна быть объектом LineString.")

        return geometry.length / 1000  # Преобразование из метров в километры

    @staticmethod
    def create_buffer(geometry: Point, distance: float) -> Polygon:
        """
        Создаёт буфер вокруг точки.

        :param geometry: Точка (Point).
        :param distance: Радиус буфера в метрах.
        :return: Буфер в виде полигона.
        """
        if not isinstance(geometry, Point):
            raise ValueError("Геометрия должна быть объектом Point.")

        return geometry.buffer(distance)

    @staticmethod
    def calculate_polygon_area(geometry: Polygon) -> float:
        """
        Рассчитывает площадь полигона.

        :param geometry: Polygon.
        :return: Площадь полигона в квадратных километрах.
        """
        if not isinstance(geometry, Polygon):
            raise ValueError("Геометрия должна быть объектом Polygon.")

        return geometry.area / 1_000_000  # Преобразование из квадратных метров в квадратные километры

    @staticmethod
    def load_geojson(file_path: str) -> gpd.GeoDataFrame:
        """
        Загружает GeoJSON файл в GeoDataFrame.

        :param file_path: Путь к GeoJSON файлу.
        :return: GeoDataFrame с географическими данными.
        """
        try:
            return gpd.read_file(file_path)
        except Exception as e:
            raise IOError(f"Ошибка загрузки GeoJSON файла: {e}")

    @staticmethod
    def save_geojson(data: gpd.GeoDataFrame, file_path: str) -> None:
        """
        Сохраняет GeoDataFrame в файл формата GeoJSON.

        :param data: GeoDataFrame для сохранения.
        :param file_path: Путь для сохранения файла.
        """
        try:
            data.to_file(file_path, driver="GeoJSON")
        except Exception as e:
            raise IOError(f"Ошибка сохранения GeoJSON файла: {e}")

    @staticmethod
    def get_centroid(geometry: Polygon) -> Tuple[float, float]:
        """
        Возвращает координаты центра полигона.

        :param geometry: Polygon.
        :return: Координаты центра (широта, долгота).
        """
        if not isinstance(geometry, Polygon):
            raise ValueError("Геометрия должна быть объектом Polygon.")

        centroid = geometry.centroid
        return centroid.y, centroid.x

    @staticmethod
    def merge_geometries(geometries: List[Polygon]) -> Polygon:
        """
        Объединяет несколько геометрий в одну.

        :param geometries: Список объектов Polygon.
        :return: Объединённая геометрия в виде одного объекта Polygon.
        """
        return gpd.GeoSeries(geometries).unary_union

    @staticmethod
    def intersect_geometries(geometry1: Polygon, geometry2: Polygon) -> Polygon:
        """
        Возвращает пересечение двух геометрий.

        :param geometry1: Первая геометрия (Polygon).
        :param geometry2: Вторая геометрия (Polygon).
        :return: Пересечение геометрий (Polygon).
        """
        return geometry1.intersection(geometry2)



# TEST
# =========================
# 
if __name__ == "__main__":
    
    from shapely.geometry import Point, Polygon, LineString
    import geopandas as gpd

    # Расчёт расстояния
    coord1 = (55.7558, 37.6173)  # Москва
    coord2 = (59.9343, 30.3351)  # Санкт-Петербург
    distance = GeoUtils.haversine_distance(coord1, coord2)
    print(f"Расстояние между Москвой и Санкт-Петербургом: {distance:.2f} км")

    # Создание буфера вокруг точки
    point = Point(37.6173, 55.7558)  # Координаты Москвы
    buffer = GeoUtils.create_buffer(point, 10000)  # Буфер в 10 км

    # Вычисление площади полигона
    polygon = buffer
    area = GeoUtils.calculate_polygon_area(polygon)
    print(f"Площадь буфера: {area:.2f} км²")

    # Загрузка GeoJSON файла
    geo_data = GeoUtils.load_geojson("data\raw\countries_50m.geojson")
