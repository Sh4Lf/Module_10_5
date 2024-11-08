import time
import os
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


# Список названий файлов (замените на свои файлы)
file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt','file 4.txt']

#Линейное выполнение
# start_time_linear = time.time()
#
# for name in file_names:
#     data = read_info(name)
#
# end_time_linear = time.time()
# print(f"Время выполнения линейного подхода: {end_time_linear - start_time_linear:.2f} секунд")

# Многопроцессное выполнение
if __name__ == '__main__':
    start_time_parallel = time.time()

    with Pool() as pool:
        results = pool.map(read_info, file_names)

    end_time_parallel = time.time()
    print(f"Время выполнения многопроцессного подхода: {end_time_parallel - start_time_parallel:.2f} секунд")