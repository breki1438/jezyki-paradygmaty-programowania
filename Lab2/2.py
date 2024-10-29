import numpy as np

def MatrixOperation(operation, matrices):
    locals().update(matrices)
    
    try:
        if "+" in operation:
            m1Name, m2Name = operation.split("+")
            m1, m2 = eval(m1Name.strip()), eval(m2Name.strip())
            
            if m1.shape != m2.shape:
                raise ValueError("Niezgodne wymiary macierzy do dodawania.")
            result = m1 + m2
        
        elif "*" in operation:
            m1Name, m2Name = operation.split("*")
            m1, m2 = eval(m1Name.strip()), eval(m2Name.strip())
            
            if m1.shape[1] != m2.shape[0]:
                raise ValueError("Niezgodne wymiary macierzy do mnożenia.")
            result = m1 @ m2
        
        elif ".T" in operation:
            mName = operation.replace(".T", "").strip()
            result = eval(mName).T
        
        else:
            raise ValueError("Nieprawidłowa operacja.")
        
        return result

    except Exception as e:
        return f"Błąd wykonania: {e}"

matrices = {
    "A": np.array([[1, 2], [3, 4]]),
    "B": np.array([[5, 6], [7, 8]]),
    "C": np.array([[1, 2, 3], [4, 5, 6]])
}

print(MatrixOperation("A + B", matrices))  # Dodawanie macierzy
print(MatrixOperation("A * B", matrices))  # Mnożenie macierzy
print(MatrixOperation("A.T", matrices))    # Transpozycja macierzy