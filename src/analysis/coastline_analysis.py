import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

class CoastlineAnalyzer:
    """
    Определяет прибрежные страны и рассчитывает длину береговых линий.
    """

    def __init__(self, countries_gdf: gpd.GeoDataFrame, marine_gdf: gpd.GeoDataFrame):
        """
        Инициализация с данными о странах и морских полигонах.

        :param countries_gdf: GeoDataFrame со странами (например, world).
        :param marine_gdf: GeoDataFrame с морями/океанами (например, marine_polys).
        """
        self.countries = countries_gdf.copy()
        self.marine = marine_gdf.copy()

        # Убедимся, что CRS совпадает (если нет — приводим к CRS стран)
        if self.countries.crs != self.marine.crs:
            self.marine = self.marine.to_crs(self.countries.crs)

        # Объединяем все морские полигоны в один объект (unary_union)
        # Это упростит операции пересечения
        self.marine_union = self.marine.unary_union

    def detect_coastal_countries(self) -> gpd.GeoDataFrame:
        """
        Определяет прибрежные страны на основе пересечения их геометрий с морской поверхностью.
        Добавляет в self.countries поле 'is_coastal': True/False.

        :return: Обновлённый GeoDataFrame со столбцом 'is_coastal'.
        """
        def is_coastal(geom):
            # Если пересечение с морем непустое, значит страна прибрежная
            intersection = geom.intersection(self.marine_union)
            return not intersection.is_empty

        self.countries['is_coastal'] = self.countries['geometry'].apply(is_coastal)
        return self.countries

    def calculate_coastline_length(self, crs_for_calculation="EPSG:3857") -> gpd.GeoDataFrame:
        """
        Вычисляет длину береговой линии для каждой страны (в метрах).
        Использует проекцию crs_for_calculation (по умолчанию EPSG:3857).

        :param crs_for_calculation: Код проекции, в которой будет рассчитана длина.
        :return: GeoDataFrame c новым столбцом 'coast_length_m'.
        """
        # Создадим копии GeoDataFrame и перепроецируем
        countries_proj = self.countries.to_crs(crs_for_calculation)
        marine_union_proj = gpd.GeoSeries([self.marine_union], crs=self.countries.crs)\
                                .to_crs(crs_for_calculation).unary_union

        def coastline_length(geom):
            """
            Пересечение геометрии страны с морями и вычисление длины границы.
            """
            intersection = geom.intersection(marine_union_proj)
            # Граница пересечения (boundary) и есть береговая линия
            return intersection.boundary.length

        # Добавляем новый столбец с длиной береговой линии
        countries_proj['coast_length_m'] = countries_proj['geometry'].apply(coastline_length)

        # Переносим полученные длины обратно в исходный GeoDataFrame
        self.countries['coast_length_m'] = countries_proj['coast_length_m']
        return self.countries
