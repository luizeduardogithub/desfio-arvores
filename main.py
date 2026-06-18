class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 1


class AVL:
    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esq) - self.altura(no.dir)

    def rotacao_direita(self, y):
        x = y.esq
        t2 = x.dir

        x.dir = y
        y.esq = t2

        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))
        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))

        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        t2 = y.esq

        y.esq = x
        x.dir = t2

        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))
        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))

        return y

    def inserir(self, raiz, valor):
        if not raiz:
            return No(valor)

        if valor < raiz.valor:
            raiz.esq = self.inserir(raiz.esq, valor)
        elif valor > raiz.valor:
            raiz.dir = self.inserir(raiz.dir, valor)
        else:
            return raiz

        raiz.altura = 1 + max(
            self.altura(raiz.esq),
            self.altura(raiz.dir)
        )

        balance = self.balanceamento(raiz)

        # LL
        if balance > 1 and valor < raiz.esq.valor:
            return self.rotacao_direita(raiz)

        # RR
        if balance < -1 and valor > raiz.dir.valor:
            return self.rotacao_esquerda(raiz)

        # LR
        if balance > 1 and valor > raiz.esq.valor:
            raiz.esq = self.rotacao_esquerda(raiz.esq)
            return self.rotacao_direita(raiz)

        # RL
        if balance < -1 and valor < raiz.dir.valor:
            raiz.dir = self.rotacao_direita(raiz.dir)
            return self.rotacao_esquerda(raiz)

        return raiz

    def menor_no(self, no):
        atual = no
        while atual.esq:
            atual = atual.esq
        return atual

    def remover(self, raiz, valor):
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.esq = self.remover(raiz.esq, valor)

        elif valor > raiz.valor:
            raiz.dir = self.remover(raiz.dir, valor)

        else:
            if not raiz.esq:
                return raiz.dir

            elif not raiz.dir:
                return raiz.esq

            temp = self.menor_no(raiz.dir)
            raiz.valor = temp.valor
            raiz.dir = self.remover(raiz.dir, temp.valor)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(
            self.altura(raiz.esq),
            self.altura(raiz.dir)
        )

        balance = self.balanceamento(raiz)

        # LL
        if balance > 1 and self.balanceamento(raiz.esq) >= 0:
            return self.rotacao_direita(raiz)

        # LR
        if balance > 1 and self.balanceamento(raiz.esq) < 0:
            raiz.esq = self.rotacao_esquerda(raiz.esq)
            return self.rotacao_direita(raiz)

        # RR
        if balance < -1 and self.balanceamento(raiz.dir) <= 0:
            return self.rotacao_esquerda(raiz)

        # RL
        if balance < -1 and self.balanceamento(raiz.dir) > 0:
            raiz.dir = self.rotacao_direita(raiz.dir)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, valor):
        caminho = []

        atual = raiz

        while atual:
            caminho.append(str(atual.valor))

            if valor == atual.valor:
                print("Caminho:", " -> ".join(caminho))
                print("Elemento encontrado")
                return

            elif valor < atual.valor:
                atual = atual.esq

            else:
                atual = atual.dir

        print("Caminho:", " -> ".join(caminho))
        print("Elemento não encontrado")

    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esq)
            print(raiz.valor, end=" ")
            self.em_ordem(raiz.dir)

    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.valor, end=" ")
            self.pre_ordem(raiz.esq)
            self.pre_ordem(raiz.dir)

    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esq)
            self.pos_ordem(raiz.dir)
            print(raiz.valor, end=" ")

    def mostrar_arvore(self, raiz):
        print("Em-Ordem:", end=" ")
        self.em_ordem(raiz)
        print()


avl = AVL()
raiz = None

print("Digite comandos (i, r, b, em, pre, pos)")
print("Digite sair para encerrar")

while True:
    comando = input().strip()

    if comando.lower() == "sair":
        break

    partes = comando.split()

    if partes[0] == "i":
        valor = int(partes[1])
        raiz = avl.inserir(raiz, valor)
        avl.mostrar_arvore(raiz)

    elif partes[0] == "r":
        valor = int(partes[1])
        raiz = avl.remover(raiz, valor)
        avl.mostrar_arvore(raiz)

    elif partes[0] == "b":
        valor = int(partes[1])
        avl.buscar(raiz, valor)

    elif partes[0] == "em":
        avl.em_ordem(raiz)
        print()

    elif partes[0] == "pre":
        avl.pre_ordem(raiz)
        print()

    elif partes[0] == "pos":
        avl.pos_ordem(raiz)
        print()