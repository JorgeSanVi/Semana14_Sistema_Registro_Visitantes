# Semana14_Sistema_Registro_Visitantes

## Descripción de la tarea

Esta tarea corresponde a la semana 14 de la materia de Programación Orientada a Objetos. Consiste en el desarrollo de una aplicación de escritorio en Python con interfaz gráfica usando Tkinter, cuyo objetivo es gestionar el registro de visitantes en una oficina.

La aplicación fue desarrollada siguiendo una arquitectura modular por capas, lo que permite organizar mejor el código y separar la lógica de negocio de la interfaz gráfica. De esta manera, el programa resulta más ordenado, entendible y fácil de mantener.

## Objetivo

Desarrollar una aplicación CRUD modular que permita registrar, visualizar y eliminar visitantes, además de limpiar los campos del formulario, aplicando correctamente conceptos de Programación Orientada a Objetos como clases, constructores, encapsulamiento e inyección de dependencias.

## Funcionalidades

La aplicación permite realizar las siguientes acciones:

- Registrar un nuevo visitante.
- Visualizar los visitantes registrados en una tabla.
- Eliminar un visitante seleccionado.
- Limpiar los campos del formulario.
- Mostrar mensajes de validación y confirmación.

## Datos del visitante

Cada visitante registrado contiene los siguientes datos:

- Cédula
- Nombre completo
- Motivo de la visita

## Estructura de la tarea

La tarea fue organizado en capas para cumplir con la arquitectura solicitada:

```bash
Semana14_Sistema_Registro_Visitantes/
│
├── main.py
├── README.md
├── .gitignore
├── modelos/
│   ├── __init__.py
│   └── visitante.py
├── servicios/
│   ├── __init__.py
│   └── visita_servicio.py
└── ui/
    ├── __init__.py
    └── app_tkinter.py