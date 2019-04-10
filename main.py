# importing required modules
import PyPDF2 # https://pypi.org/project/PyPDF2/

##############################################
# EDIT THESE vvv

def getPath(s):
    pdf_dir = "C:/Users/Richard Liu/Downloads/"
    pdf_name = "hustle_{}_mu_alpha_theta_national_2016.pdf".format(s) # What file you want to fix
    pdf_name = "chicken.pdf"
    return(pdf_dir + pdf_name)

def getNewPath(s):
    pdf_dir = "C:/Users/Richard Liu/Downloads/"
    pdf_name = "hustle_{}_nats_2016-FIXED.pdf".format(s) # What you want your fixed file to be called
    pdf_name = "new-chicken.pdf"
    return(pdf_dir + pdf_name)

# EDIT THESE ^^^
##############################################

def fourth(orig_path, new_path):

    pdfFileObj = open(orig_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    

    basePage = ""
    for page in range(pdfReader.numPages):
        
        pageObj = pdfReader.getPage(page)
        
        if(page%4 == 0):
            if(page != 0):
                pdfWriter.addPage(basePage)
            basePage = pageObj.createBlankPage(pdf=pdfReader)
        
        coords = [ # May need to adjust for different files.
            [-300, 380],
            [300, 380],
            [-300, -380],
            [300, -380],
        ]

        coord = coords[page%4]
        print("merging")
        basePage.mergeTranslatedPage(pageObj, coord[0], coord[1])
    pdfWriter.addPage(basePage)
 
    # new pdf file object
    newFile = open(new_path, 'wb')
    pdfWriter.write(newFile)

    pdfFileObj.close()
    newFile.close()

##############################################
# EDIT THESE vvv

subjects = [
    "algebra",
    "calculus",
    "geometry",
    "trigonometry",
    "probability_&_statistics"
]

if __name__ == '__main__':
    for i in range(5):
        fourth(getPath(subjects[i]), getNewPath(subjects[i]))
        print("done")

# EDIT THESE ^^^
##############################################