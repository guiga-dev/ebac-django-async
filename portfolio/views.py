import asyncio
from django.http import JsonResponse

async def calcular(numero):
    print(f"Iniciando c�lculo de {numero}")
    await asyncio.sleep(0.1)
    resultado = numero * numero
    print(f"Resultado de {numero}: {resultado}")
    return resultado

async def calculos(request):
    for contador in range(1, 11):
        print(f"Contador: {contador}")
        await asyncio.sleep(0.1)
    resultados = await asyncio.gather(*(calcular(numero) for numero in range(1, 4)))
    return JsonResponse({"resultados": resultados})
