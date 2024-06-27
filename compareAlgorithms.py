import os
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from assemblyLinesBruteForce import assemblyLineBruteForce
from assemblyLinesDynamicProgramming import assemblyLinesDynamicProgrammming

def generateRandomInput(size):
    S = [[random.randint(1, 10) for _ in range(size)] for _ in range(2)]
    
    t = [[random.randint(1, 10) for _ in range(size - 1)] for _ in range(2)]

    e = [random.randint(10, 20) for _ in range(2)]

    x = [random.randint(10, 20) for _ in range(2)]
    
    return S, t, e, x

# Define input size
inputSize = 20
inputList = list(range(1, inputSize + 1))

# Create directory for results if it doesn't exist
resultsDir = 'results'
os.makedirs(resultsDir, exist_ok=True)

bruteForceExecutionTime = [0] * inputSize
dynamicExecutionTime = [0] * inputSize

for i in inputList:

    S, t, e, x = generateRandomInput(i)
    start = time.time()
    assemblyLineBruteForce(S, t, e, x, False)
    end = time.time()
    bruteForceExecutionTime[i-1] = end - start

    start = time.time()
    assemblyLinesDynamicProgrammming(S, t, e, x)
    end = time.time()
    dynamicExecutionTime[i-1] = end - start

    data = {
        'Input size': inputList,
        'Assembly Lines brute-force': bruteForceExecutionTime,
        'Assembly Lines Dynamic Programming': dynamicExecutionTime,
    }

    df = pd.DataFrame(data)

    dfName = f'{resultsDir}/dataframe-{inputSize}.xlsx'
    df.to_excel(dfName, index=False)


plt.figure(figsize=(10, 5))
plt.plot(inputList, bruteForceExecutionTime, label='Assembly Lines brute-force')
plt.plot(inputList, dynamicExecutionTime, label='Assembly Lines Dynamic Programming')
plt.xlabel('Input size')
plt.ylabel('Time (s)')
plt.title('Algorithms execution time')
plt.legend()
plt.grid(True)

figName = f'{resultsDir}/figure-{inputSize}.png'
plt.savefig(figName)

plt.show()
