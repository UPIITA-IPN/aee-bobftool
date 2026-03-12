def exp_binaria_mod(base, exponente, mod):
    resultado = 1
    base = base % mod
    
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % mod
        
        base = (base * base) % mod
        exponente //= 2
    
    return resultado

base = 2
exponente = 1234
mod = 789

print(exp_binaria_mod(base, exponente, mod))