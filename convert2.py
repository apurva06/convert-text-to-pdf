#!/usr/bin/env python

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


ptr = open("input.txt", "r")  # text file I need to convert
lineas = ptr.readlines()
ptr.close()
i = 6570
numeroLinea = 0
c = canvas.Canvas("input.pdf")
while numeroLinea < len(lineas):

    i = 6570
    for linea in lineas[numeroLinea:]:
        c.drawString(15, i, linea.strip())
        numeroLinea += 1
        i -= 10


c.showPage()
c.save()
