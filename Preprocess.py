#!/usr/bin/env python
# coding: utf-8

# In[1]:


make_model = [{'Alfa Romeo': 0,
  'Aston Martin': 1,
  'Audi': 2,
  'BMW': 3,
  'Baic': 4,
  'Bestune': 5,
  'Brilliance': 6,
  'Buick': 7,
  'Byd': 8,
  'Chana': 9,
  'Changan': 10,
  'Changhe': 11,
  'Chery': 12,
  'Chevrolet': 13,
  'Chrysler': 14,
  'Citroën': 15,
  'Cupra': 16,
  'DFSK': 17,
  'Daewoo': 18,
  'Daihatsu': 19,
  'Dodge': 20,
  'Ds': 21,
  'Exeed': 22,
  'Faw': 23,
  'Fiat': 24,
  'Ford': 25,
  'Geely': 26,
  'Great Wall': 27,
  'Hafei': 28,
  'Haima': 29,
  'Haval': 30,
  'Honda': 31,
  'Hyundai': 32,
  'Infiniti': 33,
  'Isuzu': 34,
  'Jac': 35,
  'Jaguar': 36,
  'Jeep': 37,
  'Jetour': 38,
  'Kaiyi': 39,
  'Karry': 40,
  'Kenbo': 41,
  'Keyton': 42,
  'Kia': 43,
  'Lada': 44,
  'Lancia': 45,
  'Land Rover': 46,
  'Lifan': 47,
  'MG': 48,
  'Mahindra': 49,
  'Maserati': 50,
  'Mazda': 51,
  'Mercedes': 52,
  'Mini': 53,
  'Mitsubishi': 54,
  'Nissan': 55,
  'Opel': 56,
  'Peugeot': 57,
  'Porsche': 58,
  'Proton': 59,
  'Renault': 60,
  'Saipa': 61,
  'Seat': 62,
  'Senova': 63,
  'Skoda': 64,
  'Smart': 65,
  'Soueast': 66,
  'Speranza': 67,
  'Ssang Yong': 68,
  'Subaru': 69,
  'Suzuki': 70,
  'Toyota': 71,
  'Volkswagen': 72,
  'Volvo': 73,
  'Zotye': 74},
 {'116': 0,
  '118': 1,
  '121': 2,
  '125': 3,
  '127': 4,
  '128': 5,
  '131': 6,
  '132': 7,
  '1500': 8,
  '156': 9,
  '180': 10,
  '19': 11,
  '200': 12,
  '2008': 13,
  '205': 14,
  '206': 15,
  '207': 16,
  '208': 17,
  '2105': 18,
  '2106': 19,
  '2107': 20,
  '2110': 21,
  '218 i': 22,
  '230': 23,
  '240': 24,
  '3': 25,
  '300': 26,
  '3008': 27,
  '301': 28,
  '305': 29,
  '307': 30,
  '308': 31,
  '308 sw': 32,
  '316': 33,
  '318': 34,
  '320': 35,
  '323': 36,
  '325': 37,
  '330S': 38,
  '335': 39,
  '340': 40,
  '350': 41,
  '360': 42,
  '405': 43,
  '406': 44,
  '408': 45,
  '418': 46,
  '5': 47,
  '500 X': 48,
  '5008': 49,
  '504': 50,
  '505': 51,
  '508': 52,
  '518': 53,
  '520': 54,
  '523': 55,
  '525': 56,
  '528': 57,
  '530': 58,
  '535': 59,
  '6': 60,
  '620': 61,
  '730': 62,
  '740': 63,
  '750': 64,
  '80': 65,
  '850': 66,
  '929': 67,
  'A 160': 68,
  'A 180': 69,
  'A 200': 70,
  'A1': 71,
  'A11': 72,
  'A113': 73,
  'A213': 74,
  'A3': 75,
  'A4': 76,
  'A5': 77,
  'A516': 78,
  'A6': 79,
  'A620': 80,
  'Accent': 81,
  'Accent HCI': 82,
  'Accent RB': 83,
  'Accord': 84,
  'Adam': 85,
  'Alsvin': 86,
  'Altea': 87,
  'Alto': 88,
  'Applause': 89,
  'Armada': 90,
  'Arona': 91,
  'Arrizo 5': 92,
  'Astra': 93,
  'Astro': 94,
  'Ateca': 95,
  'Atos': 96,
  'Attrage': 97,
  'Auris': 98,
  'Avante': 99,
  'Avanza': 100,
  'Avensis': 101,
  'Aveo': 102,
  'Ax': 103,
  'Azera': 104,
  'B 150': 105,
  'B 180': 106,
  'B 200': 107,
  'Baleno': 108,
  'Bayon': 109,
  'Beetle': 110,
  'Belta': 111,
  'Benni': 112,
  'Blazer': 113,
  'Bluebird': 114,
  'Bora': 115,
  'Boxster': 116,
  'Bravo': 117,
  'C 180': 118,
  'C 200': 119,
  'C 200 AMG': 120,
  'C 250': 121,
  'C 280': 122,
  'C 300': 123,
  'C Class': 124,
  'C Elysee': 125,
  'C-HR': 126,
  'C-Max': 127,
  'C3': 128,
  'C3 Aircross': 129,
  'C30': 130,
  'C31': 131,
  'C4': 132,
  'C4 Grand Picasso': 133,
  'C4 Picasso': 134,
  'C5': 135,
  'C5 Aircross': 136,
  'CC': 137,
  'CLA 180': 138,
  'CLA 200': 139,
  'CLC Class': 140,
  'CLS Class': 141,
  'CRV': 142,
  'CRX': 143,
  'CS 15': 144,
  'CS 35': 145,
  'Caddy': 146,
  'Caliber': 147,
  'Camry': 148,
  'Captiva': 149,
  'Captur': 150,
  'Carens': 151,
  'Carnival': 152,
  'Cascada': 153,
  'Cayenne': 154,
  'Cayenne S': 155,
  'Cedric': 156,
  'Ceed': 157,
  'Cerato': 158,
  'Cerato Koup': 159,
  'Charade': 160,
  'Charmant': 161,
  'Cherokee': 162,
  'Ciaz': 163,
  'City': 164,
  'Civic': 165,
  'Ck': 166,
  'Ck2': 167,
  'Clio': 168,
  'Commander': 169,
  'Cool Ray': 170,
  'Cooper': 171,
  'Cooper F55': 172,
  'Cooper Hatch': 173,
  'Cordoba': 174,
  'Corolla': 175,
  'Corona': 176,
  'Corsa': 177,
  'Country man': 178,
  'Countryman S': 179,
  'Cressida': 180,
  'Creta': 181,
  'Creta SU2': 182,
  'Cross': 183,
  'Crossland': 184,
  'Cruze': 185,
  'Crystala': 186,
  'D max': 187,
  'DS7': 188,
  'Dart': 189,
  'Dedra': 190,
  'Defender': 191,
  'Discovery sport': 192,
  'Doblo': 193,
  'Dogan': 194,
  'Ducato': 195,
  'Durango': 196,
  'Duster': 197,
  'E 180': 198,
  'E 200': 199,
  'E 200 AMG': 200,
  'E 220': 201,
  'E 230': 202,
  'E 240': 203,
  'E 250': 204,
  'E 280': 205,
  'E 300': 206,
  'E 320': 207,
  'E 350': 208,
  'E 500': 209,
  'E-2008': 210,
  'E-pace': 211,
  'EAGLE 580': 212,
  'Echo': 213,
  'Eclipse': 214,
  'Eclipse Cross': 215,
  'EcoSport': 216,
  'Elantra': 217,
  'Elantra AD': 218,
  'Elantra CN7': 219,
  'Elantra Coupe': 220,
  'Elantra HD': 221,
  'Elantra MD': 222,
  'Emgrand': 223,
  'Emgrand 7': 224,
  'Emgrand X7': 225,
  'Envy': 226,
  'Equinox': 227,
  'Ertiga': 228,
  'Escort': 229,
  'Espero': 230,
  'Excel': 231,
  'Expedition': 232,
  'F-Pace': 233,
  'F0': 234,
  'F3': 235,
  'F3R': 236,
  'FRV': 237,
  'FSV': 238,
  'Fabia': 239,
  'Familia': 240,
  'Fantasia': 241,
  'Favorit': 242,
  'Felicia': 243,
  'Felicia combi': 244,
  'Fiesta': 245,
  'Fiorino': 246,
  'Florid': 247,
  'Florida': 248,
  'Fluence': 249,
  'Flyer': 250,
  'Focus': 251,
  'Foison': 252,
  'Foreman': 253,
  'Foreste': 254,
  'Formentor': 255,
  'Forte': 256,
  'Fortuner': 257,
  'Fortwo': 258,
  'Freestar': 259,
  'Fruits': 260,
  'Fusion': 261,
  'Fx': 262,
  'GLA': 263,
  'GLC 200': 264,
  'GLC 250': 265,
  'GLC 300': 266,
  'GLE': 267,
  'GLE 350': 268,
  'GLK': 269,
  'GLK 250': 270,
  'GLK 350': 271,
  'Galant': 272,
  'Galena': 273,
  'Galloper': 274,
  'Gen 2': 275,
  'Getz': 276,
  'Ghibli': 277,
  'Glory': 278,
  'Glory 330': 279,
  'Golf': 280,
  'Golf 2': 281,
  'Golf 3': 282,
  'Golf 4': 283,
  'Golf 5': 284,
  'Golf 6': 285,
  'Golf 7': 286,
  'Grand C-Max': 287,
  'Grand Cerato': 288,
  'Grand Cherokee': 289,
  'Grand i10': 290,
  'Grand terios': 291,
  'Grandland': 292,
  'Granta': 293,
  'H1': 294,
  'H100': 295,
  'H6': 296,
  'HRV': 297,
  'HS': 298,
  'Haima 2': 299,
  'Hiace': 300,
  'Hilux': 301,
  'Hover': 302,
  'I10': 303,
  'I20': 304,
  'I30': 305,
  'IX 35': 306,
  'Ibiza': 307,
  'Ideal': 308,
  'Imperial': 309,
  'Impreza': 310,
  'Insignia': 311,
  'J7': 312,
  'JAZZ': 313,
  'JS3': 314,
  'JS4': 315,
  'Jetta': 316,
  'John Cooper': 317,
  'Jolion': 318,
  'Juke': 319,
  'Juliet': 320,
  'K5': 321,
  'K8': 322,
  'Kadjar': 323,
  'Kamiq': 324,
  'Karoq': 325,
  'Kodiaq': 326,
  'Komodo': 327,
  'Kuga': 328,
  'L3': 329,
  'Lacetti': 330,
  'Laguna': 331,
  'Lancer Crystala': 332,
  'Lancer EX Shark': 333,
  'Lancer Puma': 334,
  'Land Cruiser': 335,
  'Lanos': 336,
  'Lanos 2': 337,
  'Leganza': 338,
  'Leon': 339,
  'Liberty': 340,
  'Linea': 341,
  'Lobo': 342,
  'Lodgy': 343,
  'Logan': 344,
  'M11': 345,
  'M12': 346,
  'M50': 347,
  'M70': 348,
  'MCV': 349,
  'MZ 40': 350,
  'Macan': 351,
  'Magna': 352,
  'Malibu': 353,
  'Martin Rapide S': 354,
  'Maruti': 355,
  'Matrix': 356,
  'Mazda 2': 357,
  'Mazda 3': 358,
  'Megane': 359,
  'Meriva': 360,
  'Microbus': 361,
  'Mini Cooper S': 362,
  'Mini Truck': 363,
  'Mk': 364,
  'Mokka': 365,
  'Mondeo': 366,
  'Montero': 367,
  'Musso': 368,
  'N-Series': 369,
  'N200': 370,
  'N300': 371,
  'Naughty': 372,
  'Neon': 373,
  'New Star': 374,
  'Niva': 375,
  'Nubira 1': 376,
  'Nubira 2': 377,
  'Octavia A4': 378,
  'Octavia A5': 379,
  'Octavia A7': 380,
  'Octavia A8': 381,
  'Opirus': 382,
  'Optima': 383,
  'Optra': 384,
  'Outlander': 385,
  'PT Cruiser': 386,
  'Pajero': 387,
  'Palio': 388,
  'Pandino': 389,
  'Parati': 390,
  'Partner': 391,
  'Passat': 392,
  'Pegas': 393,
  'Peri': 394,
  'Persona': 395,
  'Petra': 396,
  'Picanto': 397,
  'Pick up': 398,
  'Pickup': 399,
  'Pointer': 400,
  'Polo': 401,
  'Polonez': 402,
  'Prado': 403,
  'Preve': 404,
  'Previa': 405,
  'Pride': 406,
  'Punto': 407,
  'Punto evo': 408,
  'Q22': 409,
  'Q3': 410,
  'Q35': 411,
  'Q7': 412,
  'Q8': 413,
  'QQ': 414,
  'QX': 415,
  'Qashqai': 416,
  'Quattroporte': 417,
  'R7': 418,
  'RX8': 419,
  'Racer': 420,
  'Rainbow': 421,
  'Ram': 422,
  'Range Rover': 423,
  'Range Rover Sport': 424,
  'Rapid': 425,
  'Rapide S': 426,
  'Rav 4': 427,
  'Regata': 428,
  'Renegade': 429,
  'Rio': 430,
  'Ritmo': 431,
  'Romeo 156': 432,
  'Romeo Giulia': 433,
  'Roomster': 434,
  'Rush': 435,
  'Rx5': 436,
  'S 320': 437,
  'S 350': 438,
  'S 400': 439,
  'S 500': 440,
  'S Presso': 441,
  'S-Type': 442,
  'S2': 443,
  'S3': 444,
  'S4': 445,
  'S5': 446,
  'S60': 447,
  'S7': 448,
  'S80': 449,
  'SEL 300': 450,
  'SIRION': 451,
  'Saga': 452,
  'Saipa': 453,
  'Samara': 454,
  'Sandero': 455,
  'Sandero Step Way': 456,
  'Santa Fe': 457,
  'Scala': 458,
  'Scorpio': 459,
  'Sentra': 460,
  'Sephia': 461,
  'Shahin': 462,
  'Shuma': 463,
  'Siena': 464,
  'Skylark': 465,
  'Solaris': 466,
  'Sonata': 467,
  'Sorento': 468,
  'Soul': 469,
  'Spark': 470,
  'Spectra': 471,
  'Splendor': 472,
  'Sportage': 473,
  'Starlet': 474,
  'Stelvio': 475,
  'Sunny': 476,
  'Superb': 477,
  'Suran': 478,
  'Swift': 479,
  'Swift Dzire': 480,
  'Sx4': 481,
  'Symbol': 482,
  'T-Series': 483,
  'T55': 484,
  'T600': 485,
  'T77 Pro': 486,
  'TXL': 487,
  'Tarraco': 488,
  'Taurus': 489,
  'Tempra': 490,
  'Tercel': 491,
  'Terios': 492,
  'Tiba': 493,
  'Tiggo': 494,
  'Tiggo 3': 495,
  'Tiggo 7': 496,
  'Tiggo 7 pro': 497,
  'Tiggo 8': 498,
  'Tiggo 8 Pro': 499,
  'Tigra': 500,
  'Tiguan': 501,
  'Tiida': 502,
  'Tipo': 503,
  'Tivoli': 504,
  'Tivoli XLV': 505,
  'Toledo': 506,
  'Town & Country': 507,
  'Trajet': 508,
  'Transit': 509,
  'Traverse': 510,
  'Trax': 511,
  'Trial Blazer': 512,
  'Tucson': 513,
  'Tucson GDI': 514,
  'Tucson Turbo GDI': 515,
  'Turan': 516,
  'UNI-T': 517,
  'Uno': 518,
  'V 40': 519,
  'V3': 520,
  'V5': 521,
  'V6': 522,
  'V60': 523,
  'V7': 524,
  'Van': 525,
  'Vectra': 526,
  'Velar': 527,
  'Veloster': 528,
  'Verna': 529,
  'Viano': 530,
  'Visto': 531,
  'Vita': 532,
  'Vitara': 533,
  'Viva': 534,
  'Voyager': 535,
  'Waja': 536,
  'Wall C30': 537,
  'Wingle 5': 538,
  'Wira': 539,
  'Wrangler': 540,
  'X1': 541,
  'X2': 542,
  'X25': 543,
  'X3': 544,
  'X35': 545,
  'X4': 546,
  'X5': 547,
  'X6': 548,
  'X7': 549,
  'X70': 550,
  'X95': 551,
  'XC 40': 552,
  'XC60': 553,
  'XC90': 554,
  'XD': 555,
  'XE': 556,
  'XTrail': 557,
  'XV': 558,
  'Xceed': 559,
  'Xpander': 560,
  'Xplosion': 561,
  'Xsara': 562,
  'Yaris': 563,
  'Yeti': 564,
  'ZS': 565}]


# In[2]:


def color_format(color):
    colors ={
        'Beige': 0,
        'Black': 1,
        'Blue': 2,
        'Bronze': 3,
        'Brown': 4,
        'Champagne': 5,
        'Cyan': 6,
        'Dark blue': 7,
        'Dark green': 8,
        'Dark red': 9,
        'Eggplant': 10,
        'Gold': 11,
        'Gray': 12,
        'Green': 13,
        'Light grey': 14,
        'Mocha': 15,
        'Olive': 16,
        'Orange': 17,
        'Petroleum': 18,
        'Purple': 19,
        'Red': 20,
        'Silver': 21,
        'White': 22,
        'Yellow': 23}
    return colors[color]

def fule_format(fule):
    fule_type = {
        'Diesel': 0, 
        'Electric': 1, 
        'Gas': 2, 
        'Hybrid': 3, 
        'Natural Gas': 4
    }
    return fule_type[fule]

def body_format(body):
    body_type = {
        '4X4': 0,
        'Coupe': 1,
        'Hatchback': 2,
        'Medium truck jumbo': 3,
        'Microbus': 4,
        'Mini Pick up': 5,
        'MiniVans': 6,
        'Pick up': 7,
        'SUV': 8,
        'Sedan': 9,
        'Van': 10,
    }
    return body_type[body]


# In[3]:


def car_age (year):
    return(2023 - year)


# In[4]:


brand_ = make_model[0]
model_ = make_model[1]


# In[5]:


def transm(trans):
    return 1 if trans.lower().strip() == 'automatic' else 0


# In[6]:


import pandas as pd
def preprossecing(inputs):
    brand = brand_[inputs['Brand']]
    model = model_[inputs['Model']]
    body = body_format(inputs['Body'])
    transmission = transm(inputs['Transmission'])
    fule = fule_format(inputs['Fule'])
    engine = inputs['Engine_CC']
    kilometer = inputs['Kilometers_Driven']
    color = color_format(inputs['Color'])
    age_car = car_age(inputs['Year'])
    
    data = pd.DataFrame({'Brand': [brand],
                         'Model': [model],
                         'Body': [body],
                         'Transmission': [transmission],
                         'Fule': [fule],
                         'Engine_CC': [engine],
                         'Kilometers_Driven': [kilometer],
                         'Color': [color],
                         'Car_Age': [age_car]})
    return data

