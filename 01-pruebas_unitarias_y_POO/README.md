# 📐 Proyecto de Figuras Geométricas - Pruebas Unitarias y POO

Este proyecto implementa clases de figuras geométricas usando Programación Orientada a Objetos (POO) y pruebas unitarias en Python.

## 🏗️ Estructura del Proyecto

```
├── main.py                    # Archivo principal del proyecto
├── README.md                  # Este archivo
├── .vscode/                   # Configuración de Visual Studio Code
│   └── settings.json
├── apps/                      # Aplicaciones 
├── data/                      # Archivos de datos e imágenes
│   ├── cilindro.jpg
│   ├── cuadrado.jpg
│   ├── piramide.png
│   ├── prisma.png
│   └── README.md
├── deps/                      # Dependencias del proyecto
│   └── README.md
├── docs/                      # Documentación del proyecto
│   └── README.md
├── modules/                   # Módulos principales
│   ├── cilindro.py           # Clase Cilindro
│   ├── cuadrado.py           # Clase Cuadrado
│   ├── piramide.py           # Clase Piramide
│   └── prisma_trapezoidal.py # Clase PrismaTrapezoidal
└── tests/                     # Pruebas unitarias
    ├── test_cilindro.py
    ├── test_cuadrado.py
    ├── test_piramide.py
    └── test_prisma.py
```

## 📚 Figuras Geométricas Implementadas
### 🟦 Cuadrado ([`modules.cuadrado`](modules/cuadrado.py))
- **Propiedades**: lado
- **Métodos**: `area()`, `perimetro()`
- **Validaciones**: lado debe ser positivo

### 🔴 Cilindro ([`modules.cilindro`](modules/cilindro.py))
- **Propiedades**: radio, altura
- **Métodos**: `volumen()`, `area_superficial()`
- **Validaciones**: radio y altura deben ser positivos

### 🔺 Pirámide ([`modules.piramide`](modules/piramide.py))
- **Propiedades**: base_longitud, altura
- **Métodos**: `volumen()`, `area_superficial()`
- **Validaciones**: base_longitud y altura deben ser positivos

### 📐 Prisma Trapezoidal ([`modules.prisma_trapezoidal`](modules/prisma_trapezoidal.py))
- **Propiedades**: base_mayor, base_menor, lado, altura_trapecio, altura_prisma
- **Métodos**: `volumen()`, `area_superficial()`
- **Validaciones**: todos los valores deben ser positivos

Algunas de esas figuras no estan implementadas por completo y queda como ejercicio completarlas

## 🧪 Pruebas Unitarias
El proyecto incluye pruebas unitarias completas para cada figura geométrica:

- [`tests/test_cuadrado.py`](tests/test_cuadrado.py) - Pruebas para la clase Cuadrado
- [`tests/test_cilindro.py`](tests/test_cilindro.py) - Pruebas para la clase Cilindro
- [`tests/test_piramide.py`](tests/test_piramide.py) - Pruebas para la clase Pirámide
- [`tests/test_prisma.py`](tests/test_prisma.py) - Pruebas para la clase PrismaTrapezoidal

Algunas de esas pruebas estan incompletas y queda como ejercicio completarlas

Para ejecutar una prueba hay que ejecutar el script de la prueba correspondiente. Tengan en cuenta de verificar las importaciones de los módulo que correspondan.

## ⚙️ Características del Proyecto

- **Encapsulamiento**: Uso de propiedades privadas con getters y setters
- **Validaciones**: Verificación de valores positivos en constructores y setters
- **Manejo de Excepciones**: Lanzamiento de `ValueError` para valores inválidos
- **Pruebas Unitarias**: prueba de funcionalidades de las clases

## 🎯 Objetivos de Aprendizaje

Este proyecto demuestra:
- Implementación de clases con POO
- Uso de propiedades y encapsulamiento
- Validación de datos de entrada
- Implementación de pruebas unitarias
- Organización modular de código
- Manejo de excepciones