import datetime
from tkinter import messagebox
import pandas as pd
from docxtpl import DocxTemplate
from os.path import exists
from docx2pdf import convert

xlsxpath= "C:/Users/joao/OneDrive/Documentos/GitHub/myideas/Python/db_example_applications.xlsx"
worddoc=DocxTemplate('Template_Volunteer_Profile.docx')

def filltemplatepdf(recordid):

    dataframe = pd.read_excel(xlsxpath)
    row_selected=dataframe.loc[dataframe['id']==recordid]
    if row_selected.empty:
        messagebox.showerror("Record not found", "The record you selected is not found in the data source")
    else:
        filling = {'txtname': row_selected['name'].values[0],
                  'txtlocation': row_selected['location'].values[0], 'txtdegree': row_selected['degree'].values[0],
                  'txtprofessionalexp': row_selected['professional experience'].values[0],
                  'txtmotivation': row_selected['motivation'].values[0], 'txtavailability': row_selected['availability'].values[0]}
        outputpathword = fr"C:\Users\joao\Downloads\templatefilled{recordid}_{datetime.date.today()}.docx"
        outputpathpdf= fr"C:\Users\joao\Downloads\templatefilled{recordid}_{datetime.date.today()}.pdf"
        worddoc.render(filling)
        worddoc.save(outputpathword)
        convert(outputpathword)

        if exists(outputpathpdf):
            messagebox.showinfo("Sucess", f"The file was safely saved in {outputpathpdf}")
        else:
            messagebox.showinfo("Cancelled", "The operation was cancelled")