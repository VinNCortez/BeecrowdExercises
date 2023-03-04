import concurrent.futures


class Calculado:
    def __init__(self, result, calls):
        self.result = result
        self.calls = calls


class Fibonacci:
    calculados = {'0': Calculado(0, 0), '1': Calculado(1, 0)}

    def get_result(self, n):
        if not str(n) in self.calculados:
            self._calcula_fib(n)
        return self.calculados[str(n)].result, self.calculados[str(n)].calls

    def _calcula_fib(self, n):
        n_str = str(n)
        if n_str in self.calculados:
            return self.calculados[n_str].result
        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                calcula_menos_um = executor.submit(self._calcula_fib, n - 1).result()
            with concurrent.futures.ThreadPoolExecutor() as executor2:
                calcula_menos_dois = executor2.submit(self._calcula_fib, n - 2).result()
            calls = self.calculados[str(n - 1)].calls + self.calculados[str(n - 2)].calls + 2

            calculado = Calculado(calcula_menos_um + calcula_menos_dois, calls)
            self.calculados[n_str] = calculado
            return calculado.result


quantidade_testes = int(input())
fib = Fibonacci()
for i in range(quantidade_testes):
    x = int(input())
    resultado, chamadas = fib.get_result(x)
    print("fib({}) = {} calls = {}".format(x, chamadas, resultado))