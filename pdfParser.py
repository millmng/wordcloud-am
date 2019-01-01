# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 04:03:31 2018

@author: milli


parse pdf for texts and clean by removing punctuation marks and special characters
does not support pdfs with non unicode characters and scan docs
"""

from tika import parser
import string

#reading old pdf files with non-unicode fonts has been imposible 
def read_pdf(path):
    raw = parser.from_file(path)
    #remove duplicated spaces and return
    return " ".join(raw['content'].split())

def clean_text(text):
    # split into words by white space
    words = text.split()    
    am_punctuation = '፠፡።፣፤፥፦፧፨“”‘’…‹‹››·•'
    am_numbers = '፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼'
    am_random = '�©'    
    to_clean = string.punctuation + am_numbers + am_random + string.ascii_letters + string.digits + am_punctuation    
    table = str.maketrans('', '', to_clean)
    stripped = [w.translate(table) for w in words]
    #remove empty strings from list
    return list(filter(None, stripped))

def parse_pdf(path):
    return clean_text(read_pdf(path))


if __name__ == '__main__':
    pass