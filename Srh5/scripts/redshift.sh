#!/bin/bash

# Si Redshift no está corriendo, lo inicia con una temperatura específica
redshift -O 3500K &
notify-send "Redshift activado: 3500K"
