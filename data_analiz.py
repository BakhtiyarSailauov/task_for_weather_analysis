import pandas as pd
import polars as pl
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('weather_data.csv')

# Преобразование температур из строк в числа
df['Temperature Day'] = df['Temperature Day'].str.replace('°', '').replace('−', '-', regex=True).astype(int)
df['Temperature Night'] = df['Temperature Night'].str.replace('°', '').replace('−', '-', regex=True).astype(int)

# Средняя температура
average_temp_day = df['Temperature Day'].mean()
average_temp_night = df['Temperature Night'].mean()

# Наиболее теплый и холодный день
warmest_day = df[df['Temperature Day'] == df['Temperature Day'].max()]['Day'].iloc[0]
coldest_day = df[df['Temperature Day'] == df['Temperature Day'].min()]['Day'].iloc[0]

# Визуализация
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Temperature Day'], label='Day Temperature')
plt.plot(df['Day'], df['Temperature Night'], label='Night Temperature')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Daily Temperatures')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Вывод результатов
print(f"Средняя дневная температура: {average_temp_day}°C")
print(f"Средняя ночная температура: {average_temp_night}°C")
print(f"Самый теплый день: {warmest_day} - день месяца")
print(f"Самый холодный день: {coldest_day} - день месяца")


# Загрузка данных в Polars DataFrame
df_pl = pl.read_csv('weather_data.csv')

# Преобразование температур в числа
df_pl = df_pl.with_columns([
    pl.col('Temperature Day').str.replace('°', '').str.replace('−', '-').cast(pl.Int32),
    pl.col('Temperature Night').str.replace('°', '').str.replace('−', '-').cast(pl.Int32)
])

# Средняя температура (Polars)
average_temp_day_pl = df_pl['Temperature Day'].mean()
average_temp_night_pl = df_pl['Temperature Night'].mean()

# Наиболее теплый и холодный день (Polars)
warmest_day_pl = df_pl.filter(pl.col('Temperature Day') == df_pl['Temperature Day'].max())['Day'].to_list()[0]
coldest_day_pl = df_pl.filter(pl.col('Temperature Day') == df_pl['Temperature Day'].min())['Day'].to_list()[0]

# Вывод результатов (Polars)
print(f"[Polars] Средняя дневная температура: {average_temp_day_pl}°C")
print(f"[Polars] Средняя ночная температура: {average_temp_night_pl}°C")
print(f"[Polars] Самый теплый день: {warmest_day_pl} - день месяца")
print(f"[Polars] Самый холодный день: {coldest_day_pl} - день месяца")
