from contextlib import redirect_stdout
from io import StringIO
from django.test import AsyncClient, SimpleTestCase

class AsyncViewTests(SimpleTestCase):
    async def test_async_calculations_and_terminal_output(self):
        output = StringIO()
        with redirect_stdout(output):
            response = await AsyncClient().get("/async/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"resultados": [1, 4, 9]})
        self.assertIn("Iniciando c�lculo de 1", output.getvalue())
        self.assertIn("Resultado de 3: 9", output.getvalue())
