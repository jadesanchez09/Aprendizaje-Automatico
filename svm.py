
# Algoritmo SVM - Máquina de vectores de soporte

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Cargar los datos
iris = load_iris()
X = iris.data
y = iris.target

# 2. Dividir datos: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Crear y entrenar el modelo SVM
modelo = SVC(kernel="linear")
modelo.fit(X_train, y_train)

# 5. Realizar predicciones
predicciones = modelo.predict(X_test)

# 6. Evaluar resultados
print("=== RESULTADOS SVM ===")
print("Exactitud:", accuracy_score(y_test, predicciones))
print("Matriz de confusión:")
print(confusion_matrix(y_test, predicciones))
print("Predicciones:", iris.target_names[predicciones])
