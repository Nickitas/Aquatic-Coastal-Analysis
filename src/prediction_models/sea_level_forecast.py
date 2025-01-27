import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class SeaLevelForecast:
    """ Прогнозирование уровня моря с использованием исторических данных, обучением модели и предсказанием изменений. """
    def __init__(self, historical_data: pd.DataFrame):
        """
        Инициализация класса с историческими данными.

        :param historical_data: pandas DataFrame с колонками ['year', 'sea_level']
        """
        self.historical_data = historical_data
        self.model = None
        self.years = None
        self.sea_levels = None

    def preprocess_data(self):
        """
        Предобработка данных: извлечение годов и уровня моря.
        """
        if 'year' not in self.historical_data.columns or 'sea_level' not in self.historical_data.columns:
            raise ValueError("Данные должны содержать колонки 'year' и 'sea_level'")
        
        self.years = self.historical_data['year'].values.reshape(-1, 1)
        self.sea_levels = self.historical_data['sea_level'].values

    def train_model(self):
        """
        Обучение линейной регрессии для прогнозирования уровня моря.
        """
        if self.years is None or self.sea_levels is None:
            self.preprocess_data()
        
        # Разделяем данные на тренировочную и тестовую выборки
        X_train, X_test, y_train, y_test = train_test_split(self.years, self.sea_levels, test_size=0.2, random_state=42)
        
        # Обучаем модель
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
        # Проверяем точность на тестовой выборке
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Ошибка модели (MSE): {mse}")

    def predict_future_levels(self, future_years: list):
        """
        Прогнозирует уровень моря для заданных годов.

        :param future_years: список годов для прогнозирования
        :return: pandas DataFrame с прогнозами
        """
        if self.model is None:
            raise ValueError("Модель не обучена. Вызовите метод train_model() перед прогнозом.")
        
        future_years_array = np.array(future_years).reshape(-1, 1)
        predictions = self.model.predict(future_years_array)
        
        return pd.DataFrame({'year': future_years, 'predicted_sea_level': predictions})

    def plot_forecast(self, future_years: list):
        """
        Строит график исторических данных и прогноза.

        :param future_years: список годов для прогноза
        """
        if self.model is None:
            raise ValueError("Модель не обучена. Вызовите метод train_model() перед построением графика.")
        
        # Прогнозируем будущие уровни моря
        predictions_df = self.predict_future_levels(future_years)
        
        # Строим график
        plt.figure(figsize=(10, 6))
        plt.scatter(self.years, self.sea_levels, color='blue', label='Исторические данные')
        plt.plot(predictions_df['year'], predictions_df['predicted_sea_level'], color='red', label='Прогноз')
        plt.xlabel('Год')
        plt.ylabel('Уровень моря (мм)')
        plt.title('Прогноз уровня моря')
        plt.legend()
        plt.grid(True)
        plt.show()





# TEST
# =========================
# import pandas as pd

# # Загружаем исторические данные
# data = pd.DataFrame({
#     'year': [1900, 1920, 1940, 1960, 1980, 2000, 2020],
#     'sea_level': [0, 5, 10, 20, 30, 50, 70]
# })

# # Инициализация класса
# forecast = SeaLevelForecast(historical_data=data)

# # Обучение модели
# forecast.train_model()

# # Прогноз уровня моря до 2100 года
# future_years = list(range(2021, 2101))
# predictions = forecast.predict_future_levels(future_years)
# print(predictions)

# # Построение графика
# forecast.plot_forecast(future_years)