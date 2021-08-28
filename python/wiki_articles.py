import wikipediaapi
import wikipedia
from fpdf import FPDF
from tqdm import tqdm
import os


def create_txt_file(text,file_name):
    file = open(f'./txt_files/{file_name}.txt','w')
    file.write(text)
    file.close()

def create_docx_file(text,file_name):
    file = open(f'./docx_files/{file_name}.docx','w')
    file.write(text)
    file.close()

def create_pdf_file(text,file_name):
    pdf = FPDF()    
    pdf.add_page()
    pdf.set_font("Arial", size = 8)
    text =  text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0,5,text,align='L',border=0)

    pdf.output(f'./pdf_files/{file_name}.pdf')



def main():

    TOTAL_NO_OF_FILES = 50
    

    if not os.path.exists('./pdf_files'):
        os.mkdir('./pdf_files')

    if not os.path.exists('./txt_files'):
        os.mkdir('./txt_files')

    if not os.path.exists('./docx_files'):
        os.mkdir('./docx_files')

    key_word = input('Enter an interesting word : ')
    try:
        topics = wikipedia.search(key_word,results = TOTAL_NO_OF_FILES)
        if(len(topics) < TOTAL_NO_OF_FILES):
            print("Turns out the word wasn't intresting enough")
            exit()
    except:
        print('Something went wrong..Plz try again!!')
        exit()


    wiki = wikipediaapi.Wikipedia('en')

    print("Topics selected : ", topics,'\n\n')

    print("Creating Files : ")
    for index in tqdm(range(len(topics))):
        text = wiki.page(topics[index]).text

        # encoding issue : latin-1 codec
        text = text.encode('latin-1', 'replace').decode('latin-1')

        if(index%3 == 0):
            create_docx_file(text,str(index))
        elif(index%3 == 1):
            create_txt_file(text,str(index))
        else:
            create_pdf_file(text,str(index))
            



if __name__ == '__main__':
    main()
