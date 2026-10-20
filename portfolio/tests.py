from contextlib import redirect_stdout
from io import StringIO
from django.test import AsyncClient, SimpleTestCase

class AsyncViewTests(SimpleTestCase):
    async def test_each_request_counts_in_terminal_and_returns_results(self):
        for _ in range(2):
            output = StringIO()
            with redirect_stdout(output):
                response = await AsyncClient().get("/async/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"resultados": [1, 4, 9]})
            contagem = [line for line in output.getvalue().splitlines() if line.startswith("Contador:")]
            self.assertEqual(contagem, [f"Contador: {numero}" for numero in range(1, 11)])
            self.assertIn("Iniciando c�lculo de 1", output.getvalue())
            self.assertIn("Resultado de 3: 9", output.getvalue())
