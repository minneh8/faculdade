paciente = 0
car = 0
neu = 0
trau = 0
ped = 0
percc = 0
percn = 0
perct = 0
percp = 0
idademax = -1000
idademin = 1000
somaidade = 0
continuar = "S"
while continuar == "S" or continuar == "s":
    try: 
        idade = int(input("Digite a idade: "))
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        imc = peso / (altura ** 2)
        espmed = ""
        while espmed != 1 and espmed != 2 and espmed != 3 and espmed != 4:
            espmed = int(input("Digite a especialidade medica (1- Cardiologia, 2- Neurologia, 3- Traumatologia, 4- Pediatria): "))
            if espmed == 1:
                print("Cardiologia")
                car = car + 1
                break
            elif espmed == 2:
                print("Neurologia")
                neu = neu + 1
                break
            elif espmed == 3:
                print("Traumatologia")
                trau = trau + 1
                break
            elif espmed == 4:
                print("Pediatria")
                ped = ped + 1
                break
            else:
                print("Por favor, digite 1, 2, 3 ou 4")
                print("Vamos tentar novamente ")
        print("-------------------------------------------------------")
        paciente = paciente + 1
        somaidade = somaidade + idade
        if idade > idademax:
            idademax = idade
        if idade < idademin:
            idademin = idade
        while continuar != "N" and continuar != "n" and continuar != "S" and continuar != "s":
            continuar = input("Deseja inserir mais um paciente ? (S/N): ")
            print("-------------------------------------------------------")
            if continuar != "N" and continuar != "n" and continuar != "S" and continuar != "s":
                print("Por favor, digite S ou N")
                print("Vamos tentar novamente ")
    except:
        print("Por favor, digite apenas numeros")
        print("Vamos tentar novamente ")

idademedia = somaidade / paciente
percc = car / paciente * 100
percn = neu / paciente * 100
perct = trau / paciente * 100
percp = ped / paciente * 100

print(f"Quantidade de pacientes: {paciente}")
print(f"Media de idade dos pacientes: {idademedia}")
print(f"Paciente mais velho cadastrado: {idademax}")
print(f"Paciente mais novo cadastrado: {idademin}")
print(f"Percentual de pacientes com Cardiologia: {percc :.2f}")
print(f"Percentual de pacientes com Neurologia: {percn :.2f}")
print(f"Percentual de pacientes com Traumatologia: {perct :.2f}")
print(f"Percentual de pacientes com Pediatria: {percp :.2f}")