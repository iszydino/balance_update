import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('output.csv')

# Lấy danh sách các tổ hợp (Kp, Ki, Kd) duy nhất
pid_sets = df[['Kp', 'Ki', 'Kd']].drop_duplicates()

# Vẽ từng biểu đồ theo từng bộ Kp, Ki, Kd
for idx, row in pid_sets.iterrows():
    kp, ki, kd = row['Kp'], row['Ki'], row['Kd']
    
    # Lọc dữ liệu tương ứng
    data = df[(df['Kp'] == kp) & (df['Ki'] == ki) & (df['Kd'] == kd)].reset_index(drop=True)
    
    # Tạo trục thời gian
    time = np.arange(len(data)) * 0.02

    # Vẽ
    plt.figure(figsize=(10, 6))
    plt.plot(time, data['pv'], label='PV', linewidth=2)
    plt.plot(time, data['P'], label='P term', linestyle='--')
    plt.plot(time, data['I'], label='I term', linestyle='-.')
    plt.plot(time, data['D'], label='D term', linestyle=':')

    # Trang trí
    plt.title(f'PID Output (Kp={kp}, Ki={ki}, Kd={kd})')
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
