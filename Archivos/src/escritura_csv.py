import csv
aviones = [
    "F-35A Lightning II",
    "F-22 Raptor",
    "F-15EX Eagle II",
    "Su-57 Felon",
    "Su-35S",
    "Chengdu J-20",
    "Shenyang J-16",
    "J-10C",
    "Eurofighter Typhoon",
    "Dassault Rafale",
    "Saab JAS 39 Gripen E",
    "KAI KF-21 Boramae",
    "MiG-35",
    "Boeing P-8A Poseidon",
    "Lockheed C-130J Super Hercules"
]

barcos = [
    "USS Gerald R. Ford (CVN-78)",
    "HMS Queen Elizabeth",
    "FS Charles de Gaulle",
    "Type 055 Nanchang",
    "Admiral Gorshkov",
    "FREMM Normandie",
    "HMAS Hobart",
    "F100 Álvaro de Bazán",
    "USS Zumwalt (DDG-1000)",
    "USS Arleigh Burke (DDG-51)",
    "Type 212A",
    "USS Virginia (SSN-774)",
    "Yasen-class Severodvinsk",
    "Type 214",
    "Pyotr Velikiy (Kirov-class)"
]

mbts = [
    "M1A2 Abrams",
    "Leopard 2A7",
    "Challenger 3",
    "Leclerc XLR",
    "K2 Black Panther",
    "Type 99A",
    "T-90M",
    "T-14 Armata",
    "Merkava Mk 4",
    "Altay",
    "Arjun Mk 1A",
    "VT-4",
    "AMX-56 Leclerc",
    "ZTZ-96B",
    "Oplot-M"
]

numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nombre_archivo = input("ingrese el nombre del documento: ")
with open(nombre_archivo, "w") as csvF:
    E = csv.writer(csvF)
    E.writerow(aviones)
    E.writerow(barcos)
    E.writerow(mbts)

