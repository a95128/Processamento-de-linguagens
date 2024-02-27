import re

texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

def iso_8601(data):
    result = re.sub(r"(3[0-1]|[0-2][0-9])/(1[0-2]|0[0-9])/([0-1][0-9][0-9][0-9]|20[0-2][0-4])", r"\3/\2/\1", texto);
    return result

print(iso_8601(texto))