# ==========================================
# ESTRUTURAS DE DADOS BASE
# ==========================================

# Estrutura para Listas Matriciais (Ex 1 ao 4)
class NoMatricial:
    def __init__(self, info=None, prox=-1):
        self.info = info
        self.prox = prox  # -1 representa o fim da lista (nulo)

# Estrutura para Lista Simplesmente Encadeada Dinâmica (Ex 5)
class NoSimples:
    def __init__(self, info):
        self.info = info
        self.prox = None

# Estrutura para Lista Duplamente Encadeada Dinâmica (Ex 6 e 7)
class NoDuplo:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None

# Estrutura para o Polinômio em LDE (Ex 8)
class NoPolinomio:
    def __init__(self, a, i):
        self.a = a       # Coeficiente
        self.i = i       # Expoente
        self.elop = None # Elo próximo (prox)
        self.eloa = None # Elo anterior (ant)


# ==========================================
# RESOLUÇÃO DOS EXERCÍCIOS
# ==========================================

# --- EXERCÍCIO 1 ---
# Contar os nós válidos de uma LUE matricial.
# Percorre a lista a partir do índice 'comeco' até encontrar o final (-1).
def exercicio1_contar_nos(memoria, comeco):
    contador = 0
    atual = comeco
    while atual != -1:
        contador += 1
        atual = memoria[atual].prox
    return contador


# --- EXERCÍCIO 2 ---
# Concatenar duas LUE matriciais.
# Percorre a lista A até o último nó e faz seu 'prox' apontar para o começo de B.
def exercicio2_concatenar_matricial(memoria, comecoA, comecoB):
    if comecoA == -1:
        return comecoB
    
    atual = comecoA
    while memoria[atual].prox != -1:
        atual = memoria[atual].prox
        
    memoria[atual].prox = comecoB
    return comecoA


# --- EXERCÍCIO 3 ---
# O primeiro elemento de A ausente em B (LUE matriciais).
def exercicio3_primeiro_ausente(memoria, comecoA, comecoB):
    atualA = comecoA
    while atualA != -1:
        valorA = memoria[atualA].info
        
        # Procura o valorA na lista B
        encontrado_em_B = False
        atualB = comecoB
        while atualB != -1:
            if memoria[atualB].info == valorA:
                encontrado_em_B = True
                break
            atualB = memoria[atualB].prox
            
        if not encontrado_em_B:
            return valorA # Retorna o primeiro que não achou
            
        atualA = memoria[atualA].prox
        
    return None # Todos os elementos de A estão em B


# --- EXERCÍCIO 4 ---
# Intercalar duas LUE ordenadas.
# Reaproveita os nós, ajustando os índices 'prox' para formar uma única lista ordenada.
def exercicio4_intercalar_matricial(memoria, comecoA, comecoB):
    # Um "nó falso" (cabeça) para facilitar as ligações
    cabeca_falsa = -2 
    ultimo = cabeca_falsa
    
    atualA = comecoA
    atualB = comecoB
    
    while atualA != -1 and atualB != -1:
        if memoria[atualA].info <= memoria[atualB].info:
            menor = atualA
            atualA = memoria[atualA].prox
        else:
            menor = atualB
            atualB = memoria[atualB].prox
            
        if ultimo == cabeca_falsa:
            comecoC = menor
        else:
            memoria[ultimo].prox = menor
        ultimo = menor
        
    # Anexa o restante da lista que não acabou
    resto = atualA if atualA != -1 else atualB
    if ultimo == cabeca_falsa:
        return resto
    else:
        memoria[ultimo].prox = resto
        
    return comecoC


# --- EXERCÍCIO 5 ---
# Inverter os apontadores de uma LUE dinâmica.
# Usa 3 ponteiros (anterior, atual, proximo) para reverter os laços in-place.
def exercicio5_inverter_lue(comeco):
    anterior = None
    atual = comeco
    
    while atual is not None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo
        
    return anterior # O novo começo é o antigo último nó


# --- EXERCÍCIO 6 ---
# Inverter os apontadores de uma LDE dinâmica.
# Troca o 'prox' pelo 'ant' de cada nó.
def exercicio6_inverter_lde(comeco):
    if comeco is None:
        return None
        
    atual = comeco
    novo_comeco = None
    
    while atual is not None:
        # Inverte os ponteiros
        temp = atual.prox
        atual.prox = atual.ant
        atual.ant = temp
        
        # O último nó visitado será o novo começo
        novo_comeco = atual
        # Como invertemos, avançamos usando o antigo 'prox' que agora está em 'ant'
        atual = atual.ant
        
    return novo_comeco


# --- EXERCÍCIO 7 ---
# Concatenar duas LDE dinâmicas.
def exercicio7_concatenar_lde(comecoA, comecoB):
    if comecoA is None:
        return comecoB
    if comecoB is None:
        return comecoA
        
    # Encontra o último nó de A
    atual = comecoA
    while atual.prox is not None:
        atual = atual.prox
        
    # Faz a dupla ligação
    atual.prox = comecoB
    comecoB.ant = atual
    
    return comecoA


# --- EXERCÍCIO 8 ---
# Avaliar um polinômio guardado em LDE.
def exercicio8_avaliar_polinomio(comeco, x):
    resultado = 0.0
    atual = comeco
    
    while atual is not None:
        # P(x) = Σ Ai * x^i
        resultado += atual.a * (x ** atual.i)
        atual = atual.elop
        
    return resultado


# ==========================================
# FUNÇÕES DE IMPRESSÃO AUXILIARES (Para testes)
# ==========================================
def print_matricial(memoria, comeco):
    atual = comeco
    elems = []
    while atual != -1:
        elems.append(str(memoria[atual].info))
        atual = memoria[atual].prox
    print(" -> ".join(elems) if elems else "Vazia")

def print_dinamica(comeco):
    atual = comeco
    elems = []
    while atual is not None:
        elems.append(str(atual.info))
        atual = atual.prox
    print(" -> ".join(elems) if elems else "Vazia")


# ==========================================
# EXECUÇÃO PRINCIPAL (TESTES)
# ==========================================
def main():
    print("=== TESTES DE LISTAS MATRICIAIS ===")
    # Simulando a "Memória" (Vetor de nós)
    memoria = [NoMatricial() for _ in range(20)]
    
    # Criando Lista A (Índices 0, 1, 2) -> Valores: 10, 20, 30
    memoria[0] = NoMatricial(10, 1)
    memoria[1] = NoMatricial(20, 2)
    memoria[2] = NoMatricial(30, -1)
    comecoA = 0
    
    # Criando Lista B (Índices 3, 4) -> Valores: 20, 40
    memoria[3] = NoMatricial(20, 4)
    memoria[4] = NoMatricial(40, -1)
    comecoB = 3

    print("\n[Ex 1] Contar nós")
    print(f"Lista A tem {exercicio1_contar_nos(memoria, comecoA)} nós.")

    print("\n[Ex 3] Primeiro ausente")
    ausente = exercicio3_primeiro_ausente(memoria, comecoA, comecoB)
    print(f"Primeiro elemento de A não presente em B: {ausente}")

    print("\n[Ex 2] Concatenar LUE Matricial")
    # Copiando memória para não estragar a lista original para os testes seguintes
    memoria_ex2 = list(memoria)
    novo_comeco_conc = exercicio2_concatenar_matricial(memoria_ex2, comecoA, comecoB)
    print("A + B: ", end="")
    print_matricial(memoria_ex2, novo_comeco_conc)

    print("\n[Ex 4] Intercalar Listas Ordenadas")
    # Recriando listas para o Ex 4 com valores ordenados diferentes
    memoria_ex4 = [NoMatricial() for _ in range(10)]
    memoria_ex4[0] = NoMatricial(1, 1); memoria_ex4[1] = NoMatricial(5, 2); memoria_ex4[2] = NoMatricial(9, -1) # Lista 1: 1 -> 5 -> 9
    memoria_ex4[3] = NoMatricial(2, 4); memoria_ex4[4] = NoMatricial(6, -1) # Lista 2: 2 -> 6
    comA = 0; comB = 3
    comC = exercicio4_intercalar_matricial(memoria_ex4, comA, comB)
    print("A intercalada com B: ", end="")
    print_matricial(memoria_ex4, comC)


    print("\n=== TESTES DE LISTAS DINÂMICAS ===")
    
    print("\n[Ex 5] Inverter LUE Dinâmica")
    n1 = NoSimples("A"); n2 = NoSimples("B"); n3 = NoSimples("C")
    n1.prox = n2; n2.prox = n3
    print("Original: ", end=""); print_dinamica(n1)
    lue_invertida = exercicio5_inverter_lue(n1)
    print("Invertida: ", end=""); print_dinamica(lue_invertida)

    print("\n[Ex 6] Inverter LDE Dinâmica")
    d1 = NoDuplo(1); d2 = NoDuplo(2); d3 = NoDuplo(3)
    d1.prox = d2; d2.ant = d1
    d2.prox = d3; d3.ant = d2
    print("Original: ", end=""); print_dinamica(d1)
    lde_invertida = exercicio6_inverter_lde(d1)
    print("Invertida: ", end=""); print_dinamica(lde_invertida)

    print("\n[Ex 7] Concatenar LDE Dinâmicas")
    # LDE 1: X -> Y
    lde_a1 = NoDuplo("X"); lde_a2 = NoDuplo("Y"); lde_a1.prox = lde_a2; lde_a2.ant = lde_a1
    # LDE 2: Z -> W
    lde_b1 = NoDuplo("Z"); lde_b2 = NoDuplo("W"); lde_b1.prox = lde_b2; lde_b2.ant = lde_b1
    lde_concatenada = exercicio7_concatenar_lde(lde_a1, lde_b1)
    print("Concatenadas: ", end=""); print_dinamica(lde_concatenada)

    print("\n[Ex 8] Avaliar Polinômio")
    # P(x) = 2x^0 + 3x^1 + 4x^2
    # Para x = 2: P(2) = 2(1) + 3(2) + 4(4) = 2 + 6 + 16 = 24
    p1 = NoPolinomio(2, 0)
    p2 = NoPolinomio(3, 1)
    p3 = NoPolinomio(4, 2)
    p1.elop = p2; p2.eloa = p1
    p2.elop = p3; p3.eloa = p2
    
    x_val = 2
    resultado = exercicio8_avaliar_polinomio(p1, x_val)
    print(f"P(x) para x={x_val} resulta em: {resultado}")

if __name__ == "__main__":
    main()
