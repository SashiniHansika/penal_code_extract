# import pdf reading library
import PyPDF2
# import regular expression library
import re

#  open penal code and put into the file object
pdfFileObj = open('data/penal_code.pdf','rb')
# Using file object create pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Regular expression to find the offense
regex_1 = r"^(.*)(Whoever)(.*)"
# Regular expression to find the punishment
regex_2 = r"^(.*)(be punished with)(.*)"

i = 27
# Get the number of pages
number_of_pages = pdfReader.numPages

# Loop start : page 27 end: 166
while i < number_of_pages:
    # create page object
    pageObj = pdfReader.getPage(i)
    # Regular expression to catch whoever para
    matches = re.finditer(regex_1, pageObj.extractText(), re.MULTILINE | re.IGNORECASE)

    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                       end=match.end(), match=match.group()))

        # Regular expression to catch "to punished with" para
        matches_1 = re.finditer(regex_2, match.group(), re.MULTILINE | re.IGNORECASE)
        for matchNum_1, match_1 in enumerate(matches_1, start=1):

            for groupNum in range(0, len(match_1.groups())):
                groupNum = groupNum + 1

                if groupNum == 1:
                    offence = match_1.group(groupNum)
                    print("offence :" , offence)

                if groupNum == 3:
                    punishment = match_1.group(groupNum)
                    print("punishment :", punishment)

    i = i+1
    print(i)

