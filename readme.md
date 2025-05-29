# 🧪 Prácticas con Selenium y Python

Este repositorio contiene prácticas desarrolladas con **Selenium y Python**, enfocadas en la automatización de pruebas web, desde conceptos básicos hasta técnicas avanzadas.

## 📚 Contenidos

1. **Primer Test con Selenium**
   - Instalación de Selenium y Pytest.
   - Creación y ejecución de un test básico.

2. **WebElements**
   - Identificación y manipulación de elementos web.
   - Uso de localizadores: ID, Name, XPath, CSS Selectors.

3. **Actions**
   - Interacciones avanzadas: clics, doble clics, arrastrar y soltar.
   - Manejo de eventos del teclado y mouse.

4. **Configuraciones del Navegador**
   - Personalización de opciones del navegador.
   - Ejecución en modo headless y manejo de perfiles.

5. **Patrones de Diseño**
   - Introducción a patrones aplicados en testing.
   - Mejores prácticas para estructurar el código de pruebas.

6. **Page Object Model (POM)**
   - Implementación del patrón POM.
   - Separación de la lógica de pruebas y la representación de páginas.

7. **BDD (Behavior Driven Development)**
   - Uso de herramientas como Behave.
   - Escritura de escenarios en lenguaje natural.

8. **Reportes con Allure**
   - Generación de reportes detallados y visuales.
   - Integración con Pytest para automatizar la creación de reportes.

9. **Configuración del `pytest.ini`**
   - Personalización de la ejecución de pruebas.
   - Definición de opciones predeterminadas y marcadores.

## 🛠️ Requisitos del Proyecto

- Python 3.8 o superior
- Selenium
- Pytest
- Allure
- Behave *(opcional, para BDD)*

Instalación de dependencias:

```bash
pip install -r requirements.txt


🧪 Ejecución de Pruebas
Para ejecutar las pruebas con pytest:

```bash
pytest

Para generar el reporte con Allure:

```bash
pytest --alluredir=reports/allure
allure serve reports/allure