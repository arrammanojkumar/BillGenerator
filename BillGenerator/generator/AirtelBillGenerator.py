import os

from utils import Utils


class AirtelBilGenerator:

    def __init__(self):
        self.project_dir = Utils.getProjectDir()
        self.output_dir = os.path.join(self.project_dir, "GeneratedFiles")
        self.resources = os.path.join(self.project_dir, "resources")

    def generate_phone_bill(self, fromDate, end, fineDate, billNumber):
        file_path = os.path.join(self.resources, "phone", "phoneBill.html")
        inFile = open(file_path, "r")
        original_content = content = inFile.read()
        inFile.close()

        dates = Utils.generate_dates(fromDate, end, fineDate, billNumber)
        for date in dates:
            content = content.replace("${FromDate}", date[0])
            content = content.replace("${BillDate}", date[1])
            content = content.replace("${FineDate}", date[2])
            content = content.replace("${BillNumber}", date[3])
            to_file_path = os.path.join(self.output_dir, "phone", date[0]+"_phoneBill.html")
            f = open(to_file_path, "w+")
            f.write(content)
            f.close()

            content = original_content

        print("Successfully Generated")
