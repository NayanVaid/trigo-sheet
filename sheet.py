from fpdf import FPDF
import math


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=15)
        self.cell(50)
        self.cell(100, 10, "Trigonometry sheet", align="C")
        self.ln(35)
   
pdf = PDF()
pdf.add_page()

deg_list=[0,7.5,15,18,30,45,60,75,90]

#Heading
pdf.set_fill_color(144, 238, 144)
pdf.cell(15,15,"Ratio",1,align="C",fill=True)
pdf.set_fill_color(255, 182, 193)

for i in deg_list:
    if i == 90:
        pdf.cell(19,15,f"{i}°",1,align="C",fill=True,ln=1)
    else:
        pdf.cell(19,15,f"{i}°",1,align="C",fill=True)

#sine
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"sin",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)
for i in deg_list:
    if i == 90:
        pdf.cell(19,15,f"{round(math.sin(math.radians(i)),2)}",1,align="C",fill=True,ln=1)
    else:
        pdf.cell(19,15,f"{round(math.sin(math.radians(i)),2)}",1,align="C",fill=True)

#cosine
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"cos",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)
for i in deg_list:
    if i == 90:
        pdf.cell(19,15,f"{round(math.cos(math.radians(i)),2)}",1,align="C",fill=True,ln=1)
    else:
        pdf.cell(19,15,f"{round(math.cos(math.radians(i)),2)}",1,align="C",fill=True)
#tan
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"tan",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)
for i in deg_list:
    if i == 90:
        pdf.cell(19,15,"N.D.",1,align="C", ln=1,fill=True)
    else:
        pdf.cell(19,15,f"{round(math.tan(math.radians(i)),2)}",1,align="C",fill=True)

#cosec
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"cosec",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)

for i in deg_list:
    if i == 0:
        pdf.cell(19,15,"N.D.",1,align="C",fill=True)
    elif i == 90:
        pdf.cell(19,15,f"{round(1/(math.sin(math.radians(i))),2)}",1,align="C",ln=1,fill=True)
    else:
        pdf.cell(19,15,f"{round(1/(math.sin(math.radians(i))),2)}",1,align="C",fill=True)

#sec
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"sec",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)
for i in deg_list:
    if i == 90:
       pdf.cell(19,15,"N.D",1,align="C", ln=1,fill=True)
    else:
        pdf.cell(19,15,f"{round(1/(math.cos(math.radians(i))),2)}",1,align="C",fill=True)


#cot
pdf.set_fill_color(255, 255, 224)
pdf.cell(15,15,"cot",1,align="C",fill=True)
pdf.set_fill_color(173, 216, 230)
for i in deg_list:
    if i == 0:
        pdf.cell(19,15,"N.D.",1,align="C",fill=True)
    elif i == 90:
        pdf.cell(19,15,f"{round(1/(math.tan(math.radians(i))),2)}",1,align="C",ln=1,fill=True)
    else:
        pdf.cell(19,15,f"{round(1/(math.tan(math.radians(i))),2)}",1,align="C",fill=True)


pdf.output("trigo_sheet.pdf")