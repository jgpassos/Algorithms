import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    root = tk.Tk()
    root.title("Leitor de Arquivo .txt")

    botao_abrir = tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo_interface)
    botao_abrir.pack(pady=80, padx=80)

    root.mainloop()

def abrir_arquivo_interface():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if file_path:
        with open(file_path, 'r') as file:
            grafo = ler_grafo(file_path)

            if grafo is not None:
                plotar_grafo(grafo, "Grafo Inicial")        
                arvore_geradora_minima = algoritmo_kruskal(grafo)
                plotar_grafo(arvore_geradora_minima, "Árvore Geradora Mínima")   
            else:
                print("Verifique se o arquivo existe e é um arquivo .txt")

def ler_grafo(file_path):
    try:
        with open(file_path, 'r') as file:
            linhas = file.readlines()
            tamanho = len(linhas)
            grafo = np.zeros((tamanho, tamanho), dtype=int)

            for i, linha in enumerate(linhas):
              vertices = [int(v) for v in linha.split(";")[0].split(",")]
              grafo[i, :len(vertices)] = vertices

            return grafo
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
    
def plotar_grafo(grafo, titulo):
    G = nx.Graph()

    for i in range(len(grafo)):
        for j in range(len(grafo[0])):
            if grafo[i][j] != 0:
                G.add_edge(i, j, weight=grafo[i][j])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(titulo)
    plt.show()

def algoritmo_kruskal(grafo):
    arvore_geradora_minima = np.zeros_like(grafo)
    vertices_visitados = np.zeros(len(grafo))

    todos_vertices_visitados = False

    while not todos_vertices_visitados:
        min_value = float('inf')
        min_i, min_j = 0, 0

        encontrado = False
        for i in range(len(grafo)):
            for j in range(len(grafo[0])):
                if grafo[i][j] != 0 and grafo[i][j] < min_value:
                    min_i, min_j = i, j
                    min_value = grafo[i][j]
                    encontrado = True

        if not encontrado:
            todos_vertices_visitados = True
            continue

        visitados = np.zeros_like(vertices_visitados)
        ciclo = busca_profundidade(arvore_geradora_minima, visitados, min_i, min_j)
        if not ciclo:
            # acíclico
            arvore_geradora_minima[min_i][min_j] = grafo[min_i][min_j]
            arvore_geradora_minima[min_j][min_i] = grafo[min_j][min_i]
            vertices_visitados[min_i] = 1
            vertices_visitados[min_j] = 1

        # retira a aresta do grafo
        grafo[min_i][min_j] = 0
        grafo[min_j][min_i] = 0

    print("Grafo obtido:\n")
    imprime_grafo_obtido(arvore_geradora_minima)

    return arvore_geradora_minima

def busca_profundidade(grafo, visitados, v_corrente, busca):
    visitados[v_corrente] = 1
    for c in range(len(grafo)):
        if grafo[v_corrente][c] != 0 and visitados[c] != 1:
            if c == busca:
                return True
            ret = busca_profundidade(grafo, visitados, c, busca)
            if ret:
                return True
    return False

def imprime_grafo_inicial(grafo):
    for i in range(len(grafo)):
        for j in range(len(grafo[0])):
            print(grafo[i][j], end=" ")
        print()

def imprime_grafo_obtido(grafo):
    for i in range(len(grafo)):
        for j in range(len(grafo[0])):
            print(grafo[i][j], " -> ", end="")
        print()

if __name__ == "__main__":
    main()
