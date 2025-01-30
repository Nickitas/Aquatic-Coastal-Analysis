import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
from typing import List

class VisualizationUtils:
    """ Модуль предназначен для работы с визуализацией данных, таких как карты, графики и пространственные изменения. """
    @staticmethod
    def plot_geodataframe(geodata: gpd.GeoDataFrame, title: str = "Карта", save_path: str = None):
        """
        Визуализирует GeoDataFrame.

        :param geodata: GeoDataFrame для отображения.
        :param title: Заголовок карты.
        :param save_path: Если указан путь, сохраняет карту в файл.
        """
        if not isinstance(geodata, gpd.GeoDataFrame):
            raise ValueError("Данные должны быть объектом GeoDataFrame.")
        
        ax = geodata.plot(figsize=(10, 8), alpha=0.6, edgecolor="k")
        plt.title(title)
        plt.xlabel("Долгота")
        plt.ylabel("Широта")
        plt.grid(True)

        if save_path:
            plt.savefig(save_path)
        plt.show()

    @staticmethod
    def plot_point_on_map(point: Point, geodata: gpd.GeoDataFrame, title: str = "Точка на карте"):
        """
        Отображает точку на карте с заданными географическими данными.

        :param point: Точка (Point), которую нужно отобразить.
        :param geodata: GeoDataFrame, представляющий фон карты.
        :param title: Заголовок карты.
        """
        if not isinstance(point, Point):
            raise ValueError("Точка должна быть объектом Point.")

        base = geodata.plot(color="white", edgecolor="black", figsize=(10, 8))
        plt.scatter([point.x], [point.y], color="red", label="Точка")
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_line_on_map(line: LineString, geodata: gpd.GeoDataFrame, title: str = "Линия на карте"):
        """
        Отображает линию на карте с заданными географическими данными.

        :param line: Линия (LineString), которую нужно отобразить.
        :param geodata: GeoDataFrame, представляющий фон карты.
        :param title: Заголовок карты.
        """
        if not isinstance(line, LineString):
            raise ValueError("Линия должна быть объектом LineString.")

        base = geodata.plot(color="white", edgecolor="black", figsize=(10, 8))
        x, y = line.xy
        plt.plot(x, y, color="blue", label="Линия")
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def visualize_polygon(polygon: Polygon, geodata: gpd.GeoDataFrame, title: str = "Полигон на карте"):
        """
        Визуализирует полигон на карте с фоном из геоданных.

        :param polygon: Полигон (Polygon), который нужно отобразить.
        :param geodata: GeoDataFrame, представляющий фон карты.
        :param title: Заголовок карты.
        """
        if not isinstance(polygon, Polygon):
            raise ValueError("Полигон должен быть объектом Polygon.")

        base = geodata.plot(color="white", edgecolor="black", figsize=(10, 8))
        x, y = polygon.exterior.xy
        plt.fill(x, y, alpha=0.5, fc="green", label="Полигон")
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_time_series(data: List[float], labels: List[str], title: str = "Временной ряд", save_path: str = None):
        """
        Построение графика временного ряда.

        :param data: Список значений временного ряда.
        :param labels: Список меток оси X.
        :param title: Заголовок графика.
        :param save_path: Если указан путь, сохраняет график в файл.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(labels, data, marker="o", label="Данные")
        plt.title(title)
        plt.xlabel("Время")
        plt.ylabel("Значения")
        plt.grid(True)
        plt.legend()

        if save_path:
            plt.savefig(save_path)
        plt.show()

    @staticmethod
    def plot_combined_map(layers: List[gpd.GeoDataFrame], colors: List[str], labels: List[str], title: str = "Комбинированная карта"):
        """
        Отображает несколько слоев GeoDataFrame на одной карте.

        :param layers: Список GeoDataFrame для отображения.
        :param colors: Список цветов для каждого слоя.
        :param labels: Список меток для легенды.
        :param title: Заголовок карты.
        """
        if len(layers) != len(colors) or len(layers) != len(labels):
            raise ValueError("Количество слоев, цветов и меток должно совпадать.")

        plt.figure(figsize=(10, 8))
        for i, layer in enumerate(layers):
            layer.plot(ax=plt.gca(), color=colors[i], label=labels[i])

        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()



# TEST
# ========================
# 
if __name__ == "__main__":
    import geopandas as gpd
    from shapely.geometry import Point, LineString, Polygon
    from utils.visualization import VisualizationUtils

    # Пример данных
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # точка
    point = Point(10, 50)
    VisualizationUtils.plot_point_on_map(point, world, title="Пример точки на карте")

    # линия
    line = LineString([(10, 50), (15, 55), (20, 50)])
    VisualizationUtils.plot_line_on_map(line, world, title="Пример линии на карте")

    # полигон
    polygon = Polygon([(10, 50), (15, 55), (20, 50), (10, 50)])
    VisualizationUtils.visualize_polygon(polygon, world, title="Пример полигона на карте")

    # временной ряд
    data = [10, 20, 15, 25, 30]
    labels = ['2020', '2021', '2022', '2023', '2024']
    VisualizationUtils.plot_time_series(data, labels, title="Пример временного ряда")
