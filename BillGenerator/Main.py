from generator.AirtelBillGenerator import AirtelBilGenerator
from utils import Utils

if __name__ == "__main__":
    print(" Welcome to Bill Generator ")
    AirtelBilGenerator().generate_phone_bill(fromDate="23-Mar-2019", end="22-Apr-2020", fineDate="11-May-2019",
                                             billNumber="718802702")
