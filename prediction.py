import joblib
import numpy as np

model = joblib.load('model.pkl')

# mendapatkan jumlah fitur yang diharapkan oleh model
expected_features = model.n_features_in_

def predict(input_data):
    # memeriksa apakah input data memiliki jumlah fitur yang sesuai
    if len(input_data) != expected_features:
        raise ValueError(f"Input data harus memiliki {expected_features} fitur, tetapi memiliki {len(input_data)} fitur.")
    
    # ubah data menjadi bentuk array dan lakukan prediksi
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

# contoh inputan
example_input_from_dataset = [0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0] 

# tambahkan nilai default (contoh: 0) agar sesuai dengan jumlah fitur yang diharapkan
if len(example_input_from_dataset) < expected_features:
    example_input_from_dataset += [0] * (expected_features - len(example_input_from_dataset))

try:
    result = predict(example_input_from_dataset)
    print(f"Yang didapat (hasil asli = No): {'Yes' if result == 1 else 'No'}")
except ValueError as e:
    print(e)
