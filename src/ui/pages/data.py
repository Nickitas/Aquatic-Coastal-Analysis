from datetime import date
from nicegui import ui
from src.ui.layout import create_layout

from src.__utils.data_loader import load_datasets
from src.ui.components.create_section_header import create_section_header


@ui.page('/data')
def data_page():
    """
    Раздел "Данные".
    Цель: дать доступ к исходным материалам проекта:
    Список/таблица с загруженными спутниковыми снимками, карты, данные со станций.
    Кнопка/иконка загрузки новых данных (upload).
    Фильтры по дате, формату, региону.
    Возможность просмотреть/открыть отдельный набор данных (для предварительного анализа или привязки к карте).
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Данные',
            subtitle='Доступ к исходным материалам проекта (спутниковые снимки, карты, станции...).',
            heading_level=1
        )

        # --------------------
        # 2. Фильтры (дата, формат, регион)
        # --------------------
        with ui.row().classes('gap-4 mb-2'):
            # Фильтр по дате (диапазон или одна дата – пример)
            start_date = ui.date(value=date.today()).props('label="С"')
            end_date = ui.date(value=date.today()).props('label="По"')

            # Фильтр по формату
            format_select = ui.select(['GeoJSON', 'Shapefile', 'GeoPackage'], value='GeoJSON', label='Формат')

            # Фильтр по региону
            region_select = ui.select(['Все регионы', 'Европа', 'Азия', 'Северная Америка'], value='Все регионы', label='Регион')

            # Кнопка "Применить фильтр"
            def apply_filters():
                ui.notify(f"Фильтры применены: с {start_date.value} по {end_date.value}, "
                          f"формат: {format_select.value}, регион: {region_select.value}")
                # Здесь вы можете обновлять таблицы/списки данными, которые подходят под фильтр
            ui.button('Применить', on_click=apply_filters) \
                .classes('bg-blue-600 text-white')

        # --------------------
        # 3. Вкладки (Спутники, Карты, Станции, Загрузка)
        # --------------------
        with ui.tabs() as tabs:
            tab_satellite = ui.tab('Спутниковые снимки')
            tab_maps = ui.tab('Карты')
            tab_stations = ui.tab('Станции')
            tab_upload = ui.tab('Загрузка')

        # Контейнеры для содержимого вкладок
        with ui.tab_panels(tabs, value=tab_satellite) as panels:

            # 3.1. Спутниковые снимки
            with ui.tab_panel(tab_satellite):
                ui.label('Список спутниковых снимков').classes('text-lg font-semibold mb-2')

                # a) Данные, которые хотим отобразить
                satellite_data = {
                    'Дата': ['2023-01-10', '2023-02-05'],
                    'Платформа': ['Sentinel-2', 'Landsat-8'],
                    'Покрытие (%)': [80, 60],
                    'Формат': ['GeoTIFF', 'GeoTIFF'],
                }
                # b) Преобразуем в columns / rows
                sat_columns = [
                    {'name': 'Дата',        'label': 'Дата'},
                    {'name': 'Платформа',   'label': 'Платформа'},
                    {'name': 'Покрытие (%)','label': 'Покрытие (%)'},
                    {'name': 'Формат',      'label': 'Формат'},
                ]
                sat_rows = []
                for i in range(len(satellite_data['Дата'])):
                    sat_rows.append({
                        'Дата': satellite_data['Дата'][i],
                        'Платформа': satellite_data['Платформа'][i],
                        'Покрытие (%)': satellite_data['Покрытие (%)'][i],
                        'Формат': satellite_data['Формат'][i],
                    })

                ui.table(columns=sat_columns, rows=sat_rows)

                # Кнопка "Открыть снимок"
                ui.button('Открыть выделенный снимок').props('flat')

            # 3.2. Карты
            with ui.tab_panel(tab_maps):
                ui.label('Наборы карт').classes('text-lg font-semibold mb-2')

                map_data = {
                    'Название': ['World Map', 'Coastal Zones'],
                    'Масштаб': ['1:50m', '1:10m'],
                    'Формат': ['GeoPackage', 'Shapefile'],
                }
                map_columns = [
                    {'name': 'Название', 'label': 'Название'},
                    {'name': 'Масштаб',  'label': 'Масштаб'},
                    {'name': 'Формат',   'label': 'Формат'},
                ]
                map_rows = []
                for i in range(len(map_data['Название'])):
                    map_rows.append({
                        'Название': map_data['Название'][i],
                        'Масштаб':  map_data['Масштаб'][i],
                        'Формат':   map_data['Формат'][i],
                    })

                ui.table(columns=map_columns, rows=map_rows)

                ui.button('Посмотреть на карте').props('flat')

            # 3.3. Станции
            with ui.tab_panel(tab_stations).classes('f-full'):
                ui.label('Данные станций').classes('text-lg font-semibold mb-2')

                stations_data = {
                    'ID станции': [101, 102, 201],
                    'Название': ['Rostov station', 'Sochi station', 'Astrakhan station'],
                    'Тип': ['Приливная', 'Метео', 'Приливная'],
                }
                station_columns = [
                    {'name': 'ID станции', 'label': 'ID станции'},
                    {'name': 'Название',   'label': 'Название'},
                    {'name': 'Тип',        'label': 'Тип'},
                ]
                station_rows = []
                for i in range(len(stations_data['ID станции'])):
                    station_rows.append({
                        'ID станции': stations_data['ID станции'][i],
                        'Название':   stations_data['Название'][i],
                        'Тип':        stations_data['Тип'][i],
                    })

                ui.table(columns=station_columns, rows=station_rows)

                ui.button('Посмотреть детали станции').props('flat')

            # 3.4. Загрузка
            with ui.tab_panel(tab_upload):
                ui.label('Загрузка новых данных').classes('text-lg font-semibold mb-2')

                # a) Лог
                log_area = ui.log(max_lines=30).classes('w-full h-56 mb-2')

                def logger(msg: str):
                    log_area.push(msg)

                # b) Кнопка "Скачать Natural Earth"
                def on_download_click():
                    load_datasets(logger=logger)
                    ui.notify('Загрузка Natural Earth завершена!')

                ui.button('Скачать Natural Earth', on_click=on_download_click) \
                    .classes('bg-blue-600 text-white mt-2')

                # c) Загрузчик локальных файлов
                def on_upload(e):
                    logger(f"Загружаю файл: {e.name} (размер: {len(e.content)} байт)")
                    ui.notify(f"Файл {e.name} успешно загружен!")

                ui.upload(on_upload=on_upload, label='Загрузить файл', auto_upload=True).props('multiple')  
                ui.label('Здесь можно загружать свои локальные данные.').classes('text-sm text-gray-600')
