# !pip install --upgrade earthaccess

import earthaccess
import logging
from datetime import datetime, timedelta

import earthaccess
print(dir(earthaccess))

def download_modis_images(sea_polygon, start_date=None, end_date=None):
    """
    Загрузка спутниковых снимков MODIS для выбранного региона
    """
    # Если даты не указаны, берем последний месяц
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')

    # Получаем координаты полигона
    bounds = sea_polygon.total_bounds

    try:
        # Авторизация
        auth = earthaccess.login(strategy="interactive")  # Или другой метод авторизации

        # Убедитесь, что коллекция соответствует вашим нуждам
        search_results = earthaccess.search_data(
            short_name="MOD09GA",  # Дневные поверхностные отражения
            bounding_box=(
                bounds[0],  # нижняя левая долгота
                bounds[1],  # нижняя левая широта
                bounds[2],  # верхняя правая долгота
                bounds[3]   # верхняя правая широта
            ),
            temporal=(start_date, end_date)
        )

        # Получаем гранулы для загрузки
        granules = list(search_results)
        if not granules:
            logging.warning("Гранулы не найдены для указанного региона и времени.")
            return []

        # Скачивание файлов
        local_files = earthaccess.download(granules)

        return [str(file) for file in local_files]

    except Exception as e:
        logging.error(f"Ошибка при загрузке снимков: {e}")
        return []