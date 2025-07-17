# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []
ordem_atendimento = []
# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordem_por_idade(lista):
   ordem_por_idade = sorted(lista,key=lambda x:x[1], reverse=True)
   return ordem_por_idade

def ordem(Lista_paciente):
  prioridade_por_idade = []
  paciente_urgente = []
  for paciente in Lista_paciente:
    if paciente[2] ==  'urgente':
        paciente_urgente.append(paciente)
    else:
        prioridade_por_idade.append(paciente)
  return paciente_urgente, prioridade_por_idade


# TODO: Exiba a ordem de atendimento com título e vírgulas:
urgentes_por_idade, comum_por_idade = ordem(pacientes)

ordem = ordem_por_idade(urgentes_por_idade) + ordem_por_idade(comum_por_idade)
for paciente in ordem:
  ordem_atendimento.append(paciente[0])
print(f"Ordem de Atendimento: " + ', '.join(ordem_atendimento))