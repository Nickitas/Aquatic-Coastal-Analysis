import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AtmosphericEffects:
    """  
    Класс для анализа влияния потоков рек и динамики льдов на морскую акваторию.
"""
    def __init__(self, river_flow_data: pd.DataFrame, ice_dynamics_data: pd.DataFrame):
        """
        Инициализация класса с данными потоков рек и динамики льдов.

        :param river_flow_data: pandas DataFrame с колонками ['date', 'river_name', 'flow_rate']
        :param ice_dynamics_data: pandas DataFrame с колонками ['date', 'region', 'ice_area']
        """
        self.river_flow_data = river_flow_data
        self.ice_dynamics_data = ice_dynamics_data

    def analyze_river_flows(self):
        """
        Анализирует динамику потоков рек и их сезонные изменения.
        """
        if 'date' not in self.river_flow_data.columns or 'flow_rate' not in self.river_flow_data.columns:
            raise ValueError("Данные потоков рек должны содержать колонки 'date' и 'flow_rate'.")

        # Преобразуем дату в формат datetime
        self.river_flow_data['date'] = pd.to_datetime(self.river_flow_data['date'])

        # Вычисляем средний поток воды по месяцам
        self.river_flow_data['month'] = self.river_flow_data['date'].dt.month
        monthly_flow = self.river_flow_data.groupby('month')['flow_rate'].mean()

        print("Средний поток воды по месяцам:")
        print(monthly_flow)

        return monthly_flow

    def analyze_ice_dynamics(self):
        """
        Анализирует изменения площади льдов по регионам.
        """
        if 'date' not in self.ice_dynamics_data.columns or 'ice_area' not in self.ice_dynamics_data.columns:
            raise ValueError("Данные льдов должны содержать колонки 'date' и 'ice_area'.")

        # Преобразуем дату в формат datetime
        self.ice_dynamics_data['date'] = pd.to_datetime(self.ice_dynamics_data['date'])

        # Вычисляем среднюю площадь льдов по месяцам
        self.ice_dynamics_data['month'] = self.ice_dynamics_data['date'].dt.month
        monthly_ice_area = self.ice_dynamics_data.groupby('month')['ice_area'].mean()

        print("Средняя площадь льдов по месяцам:")
        print(monthly_ice_area)

        return monthly_ice_area

    def visualize_river_flows(self):
        """
        Визуализирует сезонные изменения потоков рек.
        """
        monthly_flow = self.analyze_river_flows()

        # Построение графика
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_flow.index, monthly_flow.values, marker='o', label='Средний поток воды')
        plt.xlabel('Месяц')
        plt.ylabel('Поток воды (м³/с)')
        plt.title('Сезонные изменения потоков рек')
        plt.grid(True)
        plt.legend()
        plt.show()

    def visualize_ice_dynamics(self):
        """
        Визуализирует изменения площади льдов.
        """
        monthly_ice_area = self.analyze_ice_dynamics()

        # Построение графика
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_ice_area.index, monthly_ice_area.values, marker='o', label='Средняя площадь льдов')
        plt.xlabel('Месяц')
        plt.ylabel('Площадь льдов (км²)')
        plt.title('Сезонные изменения площади льдов')
        plt.grid(True)
        plt.legend()
        plt.show()

    def calculate_combined_effects(self):
        """
        Рассчитывает влияние потоков рек и динамики льдов на морскую акваторию.
        :return: pandas DataFrame с комбинированными эффектами.
        """
        # Группируем данные по месяцам
        river_effect = self.analyze_river_flows()
        ice_effect = self.analyze_ice_dynamics()

        # Объединяем эффекты
        combined_effects = pd.DataFrame({
            'month': river_effect.index,
            'average_river_flow': river_effect.values,
            'average_ice_area': ice_effect.values
        })

        # Вычисляем интегральный показатель (условно)
        combined_effects['combined_index'] = (
            combined_effects['average_river_flow'] * 0.7 +
            combined_effects['average_ice_area'] * 0.3
        )

        print("Комбинированное влияние потоков рек и динамики льдов:")
        print(combined_effects)

        return combined_effects

    def visualize_combined_effects(self):
        """
        Визуализирует комбинированное влияние потоков рек и динамики льдов.
        """
        combined_effects = self.calculate_combined_effects()

        # Построение графика
        plt.figure(figsize=(10, 6))
        plt.plot(combined_effects['month'], combined_effects['combined_index'], marker='o', label='Комбинированное влияние')
        plt.xlabel('Месяц')
        plt.ylabel('Индекс влияния')
        plt.title('Комбинированное влияние потоков рек и динамики льдов')
        plt.grid(True)
        plt.legend()
        plt.show()




# TEST
# ===================================
# 
if __name__ == "__main__":
    import pandas as pd

    # Пример данных потоков рек
    river_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
        'river_name': ['River A', 'River A', 'River A', 'River A'],
        'flow_rate': [300, 400, 500, 600]
    })

    # Пример данных динамики льдов
    ice_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
        'region': ['Region 1', 'Region 1', 'Region 1', 'Region 1'],
        'ice_area': [5000, 4000, 3000, 2000]
    })

    # Создание экземпляра класса
    atmospheric_effects = AtmosphericEffects(river_flow_data=river_data, ice_dynamics_data=ice_data)

    # Анализ данных
    atmospheric_effects.analyze_river_flows()
    atmospheric_effects.analyze_ice_dynamics()

    # Визуализация данных
    atmospheric_effects.visualize_river_flows()
    atmospheric_effects.visualize_ice_dynamics()

    # Комбинированное влияние
    combined_effects = atmospheric_effects.calculate_combined_effects()
    atmospheric_effects.visualize_combined_effects()
