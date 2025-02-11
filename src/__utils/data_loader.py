import os
import requests
import geopandas as gpd

def download_file(url: str, filepath: str, logger=print) -> None:
    """
    Скачивает файл по ссылке url и сохраняет его по пути filepath.
    Если файл уже существует, повторно не скачивает.
    Параметр logger - функция, которой отправлять сообщения (print или другой).
    """
    if not os.path.exists(filepath):
        print(f"Скачиваю: {url}")
        response = requests.get(url)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
    else:
        print(f"Файл {filepath} уже существует, пропускаем скачивание.")
        logger(f"Файл {filepath} уже существует, пропускаем скачивание.")


def load_datasets(raw_dir="data/raw", processed_dir="data/processed", logger=print):
    """
    Загружает и сохраняет данные Natural Earth о странах, морях,
    а также дополнительные данные о водных объектах (реки, озера и т.д.).
    """

    # Ссылки на разные наборы данных Natural Earth (для 50m и 10m)
    DATASETS = {
        "countries_50m": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson",
        "marine_polys_10m": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_geography_marine_polys.geojson",
        "lakes_50m": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_lakes.geojson",
        "rivers_50m": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_rivers_lake_centerlines.geojson",
    }

    # Создаём структуру папок, если её нет
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)

    # Загружаем каждый датасет
    geo_dataframes = {}
    for name, url in DATASETS.items():
        raw_path = os.path.join(raw_dir, f"{name}.geojson")
        processed_path = os.path.join(processed_dir, f"{name}.gpkg")

        # 1. Скачиваем GeoJSON в папку raw
        download_file(url, raw_path)

        # 2. Читаем при помощи GeoPandas
        print(f"Читаем GeoDataFrame из {raw_path}")
        logger(f"Читаем GeoDataFrame из {raw_path}")
        gdf = gpd.read_file(raw_path)

        # 3. Обработка/очистка данных gdf
        # Например, фильтрацию по некоторому признаку, переименование столбцов и т.д.

        # 4. Сохраняем в обработанном виде (например, в формате GeoPackage)
        print(f"Сохраняем обработанные данные в {processed_path}")
        logger(f"Сохраняем обработанные данные в {processed_path}")
        gdf.to_file(processed_path, driver="GPKG")

        # Сохраним в словарь, чтобы потом можно было использовать в коде
        geo_dataframes[name] = gdf

    return geo_dataframes



# TEST
# 
# =================
if __name__ == '__main__':
    aquatic_data = load_datasets()
    marine_objects = aquatic_data.get('marine_polys_10m', None)

    # Проверяем наличие данных в marine_objects
    if marine_objects is not None and not marine_objects.empty:
        marine_names = marine_objects['name'].fillna('Без имени').tolist()
    else:
        marine_names = []
        print("Внимание: Данные о морских объектах отсутствуют или невалидны.")


    print(aquatic_data)
    print(marine_objects)
    