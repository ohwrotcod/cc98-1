#coding:utf-8
"""
本脚本用于获取有内容的boardid
并且与自己数据库中的比较，得到还需要获取的workset
"""
from config import db,COOKIE
from EasyLogin import EasyLogin
from xinling import getPart,getBoardSize

def runsql():
    global conn
    conn=db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def getrawlist():
    a = EasyLogin(cookie=COOKIE)
    a.get("http://www.cc98.org/customboard.asp")
    return(sorted(set([int(getPart(i,"boardid=","&")) for i in a.getList("list.asp")])))

rawlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48, 49, 50, 51, 52, 57, 58, 60, 67, 68, 72, 74, 75, 77, 80, 81, 83, 84, 85, 86, 88, 91, 99, 100, 101, 102, 103, 104, 105, 114, 115, 116, 118, 119, 122, 124, 126, 127, 128, 129, 132, 133, 134, 135, 136, 139, 140, 141, 142, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 157, 158, 164, 165, 166, 169, 170, 173, 176, 178, 179, 180, 181, 182, 183, 184, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 221, 222, 223, 224, 225, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 239, 241, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 264, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 290, 292, 293, 294, 295, 296, 297, 298, 300, 303, 304, 305, 306, 307, 308, 310, 311, 312, 313, 314, 315, 316, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 339, 340, 341, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 357, 358, 359, 361, 362, 363, 364, 367, 368, 369, 371, 372, 373, 374, 375, 376, 377, 379, 382, 383, 385, 386, 391, 392, 393, 394, 395, 396, 397, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 457, 459, 460, 461, 462, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 534, 535, 536, 537, 538, 539, 540, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 610, 611, 613, 614, 615, 616, 617, 618, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 640, 642, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 731, 733, 734, 735, 736, 738, 741, 742, 743, 744, 745, 747, 748, 749, 750, 751, 752, 753, 754]

def getsizedict():
    sizedict={}
    for i in rawlist:
        size = getBoardSize(i)
        if size>0:
            sizedict[i]=size
    return(sizedict)

sizedict={7: 8, 15: 649, 16: 535, 17: 222, 19: 103, 20: 44, 21: 9, 23: 4, 25: 111, 26: 78, 28: 50, 30: 197, 36: 1, 39: 238, 41: 12, 42: 1, 47: 28, 48: 43, 49: 1, 50: 37, 52: 2, 57: 236, 58: 411, 60: 52, 67: 121, 68: 1951, 74: 224, 75: 337, 77: 62, 80: 4556, 81: 533, 83: 5, 84: 21, 85: 85, 86: 547, 88: 69, 91: 243, 99: 71, 100: 5682, 101: 213, 102: 597, 103: 46, 104: 217, 105: 91, 114: 757, 115: 82, 119: 29, 122: 43, 126: 41, 129: 7, 135: 3030, 136: 21, 139: 39, 140: 4, 142: 311, 144: 429, 145: 59, 146: 274, 147: 709, 148: 95, 149: 1, 151: 2, 152: 1238, 154: 18, 155: 55, 157: 131, 158: 481, 164: 226, 165: 37, 169: 85, 170: 115, 173: 355, 176: 39, 178: 85, 179: 75, 180: 570, 182: 4014, 183: 30, 184: 62, 186: 73, 187: 25, 188: 112, 189: 60, 190: 8, 191: 83, 192: 46, 193: 180, 194: 46, 195: 12, 198: 436, 203: 21, 204: 2, 206: 14, 207: 5, 208: 6, 211: 83, 212: 131, 213: 6, 214: 186, 216: 19, 217: 313, 222: 15, 224: 4, 226: 367, 229: 313, 231: 39, 232: 114, 233: 89, 234: 106, 235: 1524, 236: 91, 239: 114, 241: 497, 246: 91, 247: 212, 248: 711, 252: 123, 254: 15, 255: 197, 256: 48, 258: 230, 261: 99, 262: 17, 263: 369, 264: 32, 266: 51, 267: 37, 268: 20, 269: 62, 270: 38, 271: 35, 272: 29, 273: 49, 274: 57, 275: 22, 276: 38, 277: 37, 278: 62, 279: 10, 281: 20, 282: 54, 283: 75, 284: 270, 285: 104, 286: 15, 287: 22, 288: 97, 290: 39, 292: 1, 294: 84, 295: 31, 296: 659, 303: 9, 304: 63, 306: 31, 307: 179, 308: 84, 310: 23, 311: 1, 312: 90, 314: 179, 315: 17, 316: 58, 318: 377, 319: 214, 320: 147, 321: 64, 323: 134, 324: 17, 325: 5, 326: 76, 328: 375, 329: 107, 330: 61, 331: 18, 334: 51, 339: 467, 341: 72, 344: 78, 346: 7, 347: 26, 351: 45, 352: 155, 353: 45, 355: 26, 357: 1692, 361: 36, 362: 11, 369: 8, 371: 156, 372: 61, 374: 91, 375: 8, 377: 66, 383: 58, 391: 54, 392: 35, 393: 23, 399: 1383, 401: 142, 402: 21, 403: 42, 404: 5, 405: 35, 406: 44, 410: 1, 411: 44, 413: 4, 414: 10, 415: 3, 416: 1, 417: 58, 418: 1, 422: 28, 424: 2, 425: 5, 426: 6, 428: 1, 429: 1, 430: 23, 431: 45, 432: 1, 434: 9, 436: 7, 437: 70, 440: 1, 443: 7, 444: 28, 445: 19, 446: 2, 447: 17, 448: 1, 449: 37, 450: 4, 451: 5, 452: 3, 454: 1, 455: 31, 457: 1, 459: 2781, 460: 12, 462: 78, 464: 9, 465: 32, 467: 55, 468: 20, 469: 34, 471: 92, 472: 59, 473: 84, 474: 24, 475: 27, 476: 15, 477: 43, 478: 35, 479: 26, 480: 26, 481: 30, 482: 26, 483: 23, 484: 41, 485: 31, 486: 10, 487: 25, 488: 33, 489: 20, 490: 99, 491: 17, 492: 27, 493: 21, 494: 1, 495: 20, 496: 20, 497: 37, 498: 22, 499: 10, 501: 1, 502: 14, 503: 17, 504: 37, 505: 6, 506: 26, 507: 53, 509: 108, 511: 8, 513: 1, 514: 2, 515: 1190, 516: 1, 517: 1, 518: 21, 519: 63, 520: 18, 535: 8, 537: 1236, 538: 80, 540: 2, 544: 1, 545: 34, 546: 6, 548: 2, 549: 49, 550: 11, 551: 89, 552: 25, 553: 2, 554: 1, 555: 3, 557: 24, 559: 1, 560: 204, 562: 3246, 563: 1034, 564: 23, 568: 1, 569: 26, 572: 272, 574: 7, 576: 68, 578: 5, 579: 3, 580: 79, 581: 731, 583: 18, 584: 25, 585: 20, 587: 17, 588: 5, 589: 11, 590: 1, 591: 15, 592: 37, 593: 175, 594: 192, 595: 45, 596: 14, 597: 4, 598: 90, 599: 25, 600: 1, 601: 21, 602: 2, 603: 1, 610: 4, 611: 6, 613: 4, 615: 17, 616: 14, 618: 12, 620: 5, 621: 28, 622: 60, 623: 20, 624: 25, 625: 12, 626: 2, 628: 49, 629: 1, 630: 20, 631: 1, 632: 1, 633: 1, 634: 3, 636: 6, 637: 3, 640: 1, 642: 9, 710: 3, 711: 22, 712: 1, 713: 22, 714: 1, 716: 2, 717: 3, 718: 1, 719: 1, 720: 1, 721: 2, 722: 1, 723: 3, 724: 1, 725: 2, 726: 2, 727: 2, 728: 1, 734: 1, 735: 1, 736: 5, 741: 23, 742: 12, 743: 15, 744: 21, 747: 4, 748: 6, 749: 132, 750: 1, 752: 1, 754: 1}

def getpagesum():
    pagesum=0
    for i,j in sizedict.items():
       pagesum+=j
    return(pagesum)

rawlist2=sizedict.keys()

def getworkset():
    conn=db()
    workset=[]
    for i in rawlist2:
        try:
            runsql("desc bigbbs_{}".format(i))
        except:#表不存在就说明我要get咯，加入workset
            workset.append(i)
    return(workset)

if __name__ == "__main__":
    print(getworkset())